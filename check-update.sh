#!/bin/sh
curl -L https://sourceforge.net/projects/gnurobbo/files/gnurobbo/ 2>/dev/null |grep files/latest/download |sed -e 's,.*gnurobbo-,,;s,-source.*,,'
