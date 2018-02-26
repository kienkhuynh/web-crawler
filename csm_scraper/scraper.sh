url="$1"
wget --spider --force-html -r -l2 $url 2>&1 \
  | grep '^--' | awk '{ print $3 }' \
  | grep -v '\.\(css\|js\|png\|gif\|jpg\)$' \
  > urls.m3u

