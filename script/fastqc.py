import snakemake
from snakemake.shell import shell
input1=snakemake.input.input1
input2=snakemake.input.input2
input3=snakemake.input.input3
input4=snakemake.input.input4
input5=snakemake.input.input5
input6=snakemake.input.input6
output=snakemake.output
#outdir = snakemake.output.outdir

#shell(f"fastqc {input1} {input2} {input3} {input4} {input5} {input6} --outdir {outdir} --threads 8")
shell(f"fastqc {input1} {input2} {input3} {input4} {input5} {input6} --threads 8")

