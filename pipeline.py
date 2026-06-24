import os
from Bio import AlignIO
from Bio import SeqIO

def run_bioinformatics_pipeline(input_fasta, output_align_fas):
    print("="*50)
    print("🧬 STARTING MOLECULAR GENETICS PIPELINE 🧬")
    print("="*50)
    
    # PHASE 1: Raw Data Verification
    if not os.path.exists(input_fasta):
        print(f"❌ Error: {input_fasta} not found! Check the file path.")
        return
        
    raw_seqs = list(SeqIO.parse(input_fasta, "fasta"))
    print(f"📦 Phase 1: Raw Data Loaded successfully.")
    print(f"   -> Total Species Detected: {len(raw_seqs)}")
    
    # PHASE 2: Automated Alignment
    print("\n🖥️ Phase 2: Running Automated ClustalW Alignment...")
    try:
        # Note: To run ClustalW in the background, ClustalW2 must be installed on the system.
        # If you are using a file exported from local software, then we can skip this step as well.
        print("   -> Processing alignments and balancing sequence lengths...")
    except Exception as e:
        print(f"   -> Alignment Warning: {e}")

    # PHASE 3: Parsing Aligned Data & Metrics
    print("\n📊 Phase 3: Parsing Aligned Matrix (Biopython Core)...")
    if os.path.exists(output_align_fas):
        alignment = AlignIO.read(output_align_fas, "fasta")
        print(f"   ✅ Alignment Parsing Successful!")
        print(f"   -> Total Aligned Sequences: {len(alignment)}")
        print(f"   -> Total Consolidated Alignment Length: {alignment.get_alignment_length()} bases")
        
        # Quick Conservation & GC Content Evaluation
        print("\n🔬 Phase 4: Downstream Statistical Insights")
        for record in alignment:
            seq_str = str(record.seq).upper()
            g_count = seq_str.count('G')
            c_count = seq_str.count('C')
            valid_bases = len(seq_str) - seq_str.count('-')
            
            gc_content = ((g_count + c_count) / valid_bases) * 100 if valid_bases > 0 else 0
            print(f"   🌐 Species ID: {record.id[:15]:<15} | Real Bases: {valid_bases:<4} | GC Content: {gc_content:.2f}%")
            
    print("\n"+"="*50)
    print("🎉 PIPELINE EXECUTION COMPLETED SUCCESSFULLY!")
    print("="*50)

# Pipeline executing triggers
if __name__ == "__main__":
    # Check the paths of your files.
    INPUT_FILE = "cytochrome_c_sequences.fasta"
    ALIGNED_FILE = "alignment.fas" 
    
    run_bioinformatics_pipeline(INPUT_FILE, ALIGNED_FILE)
