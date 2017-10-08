#!/usr/bin/env bash


# remove the git index
[ -f .git/index ] && rm .git/index || true

rm -rf dist *egg-info || true

find ./ -name '__pycache__' -exec rm -rf {} \; || true


set nounset
set errexit

function replace {
    from=$1
    to=$2

    for d in `find ./ -depth -type d`
    do
        new=`echo $d | sed "s/$from/$to/g"`
        [ "$d" != "$new" ] && mv $d $new
    done

    for f in `find ./ -type f`
    do
        new=`echo $f | sed "s/$from/$to/g"`
        [ "$f" != "$new" ] && mv $f $new
    done

    for f in `find ./ -type f -not -name '.git' -not -name 'rename_plugin.sh'`
    do
        sed -i "s/$from/$to/g" $f
    done

}

# RENAME THE PLUGIN
replace "_tutorial"  "_data_dms"
replace "-tutorial" "-data-dms"

replace "_TUTORIAL" "_DATA_DMS"
replace "-TUTORIAL" "-DATA-DMS"

replace "Tutorial" "DataDms"
replace "tutorial" "dataDms"

# RENAME THE STRING INT OBJECT
replace "_string_int"  "_thing_one"
replace "-string-int" "-thing-one"

replace "STRING_INT" "THING_ONE"
replace "STRING-INT" "THING-ONE"

replace "StringInt" "ThingOne"
replace "stringInt" "thingOne"

replace "String Int" "Thing One"

# Remove compile generated javascript
find ./ -type f -not -name '.git' -name "*.js" -exec rm {} \; || true
find ./ -type f -not -name '.git' -name "*.js.map" -exec rm {} \; || true
