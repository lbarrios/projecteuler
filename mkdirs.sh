#!/usr/bin/bash

for ((i=6;i<=100;i++));
do
    mkdir -p $i
    echo "# Problem $i" > $i/README.md
    echo "## Problem Title" >> $i/README.md
    echo '```' >> $i/README.md
    echo '' >> $i/README.md
    echo '```' >> $i/README.md
    echo "#!/usr/bin/env python" > $i/$i.py
done
