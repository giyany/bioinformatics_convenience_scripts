# bioinformatics_convenience_scripts
Messy, non-generic, untested, worked at some point. 

```
A couple of one-liners
```
### Delete VCFs with no records in current dir
##find the minimum nr of lines and assign; remove all VCFs with the min nr of lines


nullvcf=$(wc -l *.vcf | awk '{print $1}' | sort -n | head -1); wc -l *.vcf | awk -v l=$nullvcf '$1==l {print $2}' | xargs rm;

