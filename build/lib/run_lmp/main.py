
import glob
import os
import toml
import shutil
from jinja2 import Template
import argparse


def run(tomlfile):
    d = toml.load(tomlfile)

    for key in d:
        if "path" in key and d[key][0] != "/":
            d[key] = "/".join([os.getcwd(),d[key]])
            print("\n",d[key],"\n")

    locs = sorted( glob.glob(d["path_jobs"], recursive = True) )

    print("Found paths\n",locs,"\n\n")

    d["cores"] = d["n"]*d["c"]

    with open(d["path_job_template"], 'r') as f:
        template = Template(f.read())
    
    jobs = [ [ os.path.dirname(loc), os.path.basename(loc) ] for loc in locs]

    os.makedirs("job_files",exist_ok=True)

    for i,job in enumerate(jobs):
        print("\nExectued job folder\n",job[0])
        d["job"]     = job
        d["jobname"] = "%s_%d"%(d["name"],i)
        d["out"]     = "LOG_%s"%d["jobname"]
        run          = "job_files/run_%d.sh"%i
        with open(run, 'w') as f: f.write(template.render( x=d  ))
        console       = " ".join( [ d["submit"] ,run ] )
        print(console,"\n")
        os.system( console  )

def cli():
    parser = argparse.ArgumentParser(prog='Run LAMMPS on cluster')
    parser.add_argument(
        'path', type=str, help='path to toml file with running info')
    parser.set_defaults(func=run)
    args = parser.parse_args()

    if not os.path.isfile(args.path):
        print('The toml file specified does not exist: \n',args.path)
        sys.exit(0)
    print(args)
    return args

def main():
    args = cli()
    args.func(args.path)