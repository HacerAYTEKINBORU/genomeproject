


rule all:
    input:
        #"output/tRNA_scan_result.txt",
        #"output/G_intestinalis.tRNA"
        "output/fastqc/SRR8895272.fastq.gz.html",


rule fastqc:
    input:
        input1="resource/fastqc/SRR8895272.fastq.gz",
        input2="resource/fastqc/SRR8895273.fastq.gz",
        input3="resource/fastqc/SRR8895274.fastq.gz",
        input4="resource/fastqc/SRR8895275.fastq.gz",
        input5="resource/fastqc/SRR8895276.fastq.gz",
        input6="resource/fastqc/SRR8895277.fastq.gz",

    output:
          "output/fastqc/SRR8895272.fastq.gz.html"
          #directory("output/fastqc/"),
    conda: "env/spiro.yaml"
    script: "script/fastqc.py"
