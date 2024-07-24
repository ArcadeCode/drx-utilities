import pkg_resources
from subprocess import run
from concurrent.futures import ThreadPoolExecutor, as_completed

def update_package(package):
    '''Try to update a package and return the result'''
    try:
        result = run(["pip", "install", "--upgrade", "-qqq", package], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error when updating {package}: {result.stderr}")
        else:
            print(f"\rPackage updated : {package}", end="")
    except Exception as e:
        print(f"Exception when updating {package}: {e}")

# Get all installed packages
packages = [dist.project_name for dist in pkg_resources.working_set]
nbPackages = len(packages)
print(f"Found {nbPackages} packages...")

# Update packages with concurrent parallelism
with ThreadPoolExecutor() as executor:
    futures = [executor.submit(update_package, package) for package in packages]
    for i, future in enumerate(as_completed(futures), 1):
        print(f" \t{i}/{nbPackages} ({round((i*100)/nbPackages)}%)",)

# End with cleaning pip cache
print("Clear pip cache...")
try:
    result = run(["pip", "cache", "purge"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error when cleaning the cache : {result.stderr}")
    else:
        print(f"Cache cleared")
except Exception as e:
    print(f"Exception when cleaning the cache : {e}")