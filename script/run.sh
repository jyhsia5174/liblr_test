#! /bin/bash
num_core=8
#e='1e-3'
e='1e-4'
#e='1e-5'
#e='1e-7'

case $1 in 
  110)
    t=11
    s='0'
    log_path='log/s0_old'.$e
    ext='s0old'
    ;;
  112)
    t=11
    s='2'
    log_path='log/s2_old'.$e
    ext='s2old'
    ;;
  120)
    t=12
    s='0'
    log_path='log/s0_new'.$e
    ext='s0new'
    ;;
  122)
    t=12
    s='2'
    log_path='log/s2_new'.$e
    ext='s2new'
    ;;
  *)
    echo "Not match"
    exit 1
esac

mkdir -p $log_path
grid()
{
for f in "`./small_data.sh binary`"
do
  echo "./train -s ${s} -e ${e} -C -t ${t} ${f} > $log_path/${f#*/}.$e.$ext &"
done
}

#grid
grid | xargs -P $num_core -I {} sh -c {} &
