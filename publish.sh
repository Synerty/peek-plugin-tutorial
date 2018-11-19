#!/usr/bin/env bash

set -o nounset
set -o errexit

#------------------------------------------------------------------------------
# Configure package preferences here
PY_PACKAGE="peek_plugin_tutorial"

# Leave blank not to publish
# Or select one of the index servers defined in ~/.pypirc
PYPI_PUBLISH=""


#------------------------------------------------------------------------------
PIP_PACKAGE=${PY_PACKAGE//_/-} # Replace _ with -
HAS_GIT=`ls -d .git 2> /dev/null`


if ! [ -f "setup.py" ]; then
    echo "setver.sh must be run in the directory where setup.py is" >&2
    exit 1
fi

VER="${1:?You must pass a version of the format 0.0.0 as the only argument}"

if [ $HAS_GIT ]; then
    if [ -n "$(git status --porcelain)" ]; then
        echo "There are uncomitted changes, please make sure all changes are comitted" >&2
        exit 1
    fi

    if git tag | grep -q "${VER}"; then
        echo "Git tag for version ${VER} already exists." >&2
        exit 1
    fi
fi

#------------------------------------------------------------------------------
echo "Setting version to $VER"

# Update the setup.py
sed -i "s;^package_version.*=.*;package_version = '${VER}';"  setup.py

function updateFileVers {
    VER_FILES=""
    VER_FILES="${VER_FILES} ${PY_PACKAGE}/__init__.py"
    VER_FILES="${VER_FILES} ${PY_PACKAGE}/plugin_package.json"

    for file in ${VER_FILES}
    do
        sed -i "s/###PEEKVER###/${VER}/g" $file
        sed -i "s/111.111.111/${VER}/g" $file
    done
}

if [ $HAS_GIT ]; then
    # Upload to test pypi
    # Commit the version number to setup.py
    # This is needed for setup develop
    git commit -a -m "Updated to version ${VER}"

    # Apply the version to the other files
    updateFileVers

    # Create the package and upload to pypi
    python setup.py sdist --format=gztar upload

    # Reset all the other versions, except setup.py
    git reset --hard

    # Tag the release
    git tag ${VER}
    git push
    git push --tags
fi



#------------------------------------------------------------------------------
# Copy to local release dir if it exists
RELEASE_DIR=${RELEASE_DIR-/media/psf/release}
if [ -d  $RELEASE_DIR ]; then
    rm -rf $RELEASE_DIR/${PIP_PACKAGE}*.gz || true
    cp ./dist/${PIP_PACKAGE}-$VER.tar.gz $RELEASE_DIR
fi

