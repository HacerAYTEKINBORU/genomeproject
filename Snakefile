configfile: "env/config.yaml"

rule all:
    input: "output/tRNA_scan_result.txt",
           "output/G_intestinalis.tRNA"

rule fastqc:
    input:
        input1="resource/SRR8895272.fastq.gz",
        input2="resource/SRR8895273.fastq.gz",
        input3="resource/SRR8895274.fastq.gz",
        input4="resource/SRR8895275.fastq.gz",
    output: directory("output/fastqc"),
    conda: "env/spiro.yaml"
    script: "script/fastqc.py"
