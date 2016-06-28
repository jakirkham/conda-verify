from __future__ import print_function, division, absolute_import

from os.path import isfile, join
from optparse import OptionParser

from conda_verify.recipe import validate_recipe
from conda_verify.package import validate_package


def main():
    p = OptionParser()

    p.add_option('-v', "--verbose",
                 action="store_true")

    opts, args = p.parse_args()

    for path in args:
        if isfile(join(path, 'meta.yaml')):
            if opts.verbose:
                print("==> %s <==" % path)
            validate_recipe(path)

        elif path.endswith('.tar.bz2'):
            if opts.verbose:
                print("==> %s <==" % path)
            validate_package(path)

        else:
            if opts.verbose:
                print("Ignoring: %s" % path)


if __name__ == '__main__':
    main()