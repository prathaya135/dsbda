import sys
prev_word=None
prec_count=0

for line in sys.stdin:
    line=line.strip()
    word,count=line.split('\t')
    count=int(count)
    if prev_word==word:
        prec_count+=count
    else:
        if prev_word:
            print('%s\t%s'%(prev_word,prec_count))
        prec_count=count
        prev_word=word

if prev_word==word:
    print('%s\t%s'%(prev_word,prec_count))
