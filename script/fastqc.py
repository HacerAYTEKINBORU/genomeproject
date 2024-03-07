from snakemake.shell import shell
input1=snakemake.input.input1
input2=snakemake.input.input2
input3=snakemake.input.input3
input4=snakemake.input.input4

output=snakemake.output

shell(f"fastqc {input1} {input2} {input3} {input4} {output} --threads 8")
