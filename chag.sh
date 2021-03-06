#!/bin/sh
skip=44

tab='	'
nl='
'
IFS=" $tab$nl"

umask=`umask`
umask 77

gztmpdir=
trap 'res=$?
  test -n "$gztmpdir" && rm -fr "$gztmpdir"
  (exit $res); exit $res
' 0 1 2 3 5 10 13 15

if type mktemp >/dev/null 2>&1; then
  gztmpdir=`mktemp -dt`
else
  gztmpdir=/tmp/gztmp$$; mkdir $gztmpdir
fi || { (exit 127); exit 127; }

gztmp=$gztmpdir/$0
case $0 in
-* | */*'
') mkdir -p "$gztmp" && rm -r "$gztmp";;
*/*) gztmp=$gztmpdir/`basename "$0"`;;
esac || { (exit 127); exit 127; }

case `echo X | tail -n +1 2>/dev/null` in
X) tail_n=-n;;
*) tail_n=;;
esac
if tail $tail_n +$skip <"$0" | gzip -cd > "$gztmp"; then
  umask $umask
  chmod 700 "$gztmp"
  (sleep 5; rm -fr "$gztmpdir") 2>/dev/null &
  "$gztmp" ${1+"$@"}; res=$?
else
  echo >&2 "Cannot decompress $0"
  (exit 127); res=127
fi; exit $res
��	Vchag.sh �T[OA}�_񱴅
��m���P|�}0�l�lg�����
^��"����������v�>���I�
���}s�|�̞��.9�����@q	i�޼N���oJ��C�b&|)��Y�$΃�I�3���n7�ܕjk����ڨ~��y��W�{ݕ���{�^��E�B:�)�ج֚�^����6C���8��`O�t�D Ļ0��D�M��
~���̩�~<sk_[���r��x�������6o����qe(-����O(�D�dPH)'��W����Ɂ��<C�J\<�\k덷�ھ��;ӵ^�`��y T�C`�0)HG��n���k�S���XS��l*�����l���k���B�F/_�r	¬���F&&��v
�v�G����~h~��z��%��9�Tv�K�w����o��=�GN��a�`ߞ�m��e*�i�(��1Vh��
���(��L��jV��z����i�c��X&�iA��mD�0.�cf�H�+4n��Y��e��b��&�;����	�/��A$�GsӧP�,�����O�{���'���&QM�cj2c鋩C ��}��*7l�kh���u4���&Y�AE�p�"H{�:��a����p��ODPI�ŊnL�5���&sz���I��C�ܘa�"v��`Kf��&�I5�J��F|��	��8�ڮ�u���o�m;z���m~������'J�Y����t\q(�ɤԔ"_-���.J��"t���  