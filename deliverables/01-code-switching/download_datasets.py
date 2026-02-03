"""
Quick script to download and explore datasets for Deliverable 01.
Run this to get started with data samples for code-switching evaluation.

Requirements:
    pip install datasets huggingface_hub

Usage:
    python download_datasets.py
"""

from datasets import load_dataset
import json
from pathlib import Path

# Output directory for dataset info
OUTPUT_DIR = Path(__file__).parent / "dataset_explorations"
OUTPUT_DIR.mkdir(exist_ok=True)


def explore_dataset(dataset_name, output_file):
    """Download and explore a HuggingFace dataset."""
    print(f"\n{'='*60}")
    print(f"Exploring: {dataset_name}")
    print(f"{'='*60}")
    
    try:
        # Load dataset
        print(f"Loading dataset...")
        dataset = load_dataset(dataset_name)
        
        # Print basic info
        print(f"\nDataset structure:")
        print(dataset)
        
        # Get first sample if available
        if 'train' in dataset:
            print(f"\nFirst sample from 'train' split:")
            first_sample = dataset['train'][0]
            print(json.dumps(first_sample, indent=2, ensure_ascii=False))
            
            # Save to file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Dataset: {dataset_name}\n")
                f.write(f"{'='*60}\n\n")
                f.write(f"Structure:\n{dataset}\n\n")
                f.write(f"First sample:\n{json.dumps(first_sample, indent=2, ensure_ascii=False)}\n")
        
        print(f"\n✓ Dataset info saved to: {output_file}")
        return dataset
        
    except Exception as e:
        print(f"✗ Error loading dataset: {e}")
        return None


def main():
    """Main function to explore datasets."""
    print("Data Samples Download Script for Deliverable 01")
    print("=" * 60)
    
    datasets_to_explore = [
        ("MohamedRashad/arabic-english-code-switching", "arabic_english_codeswitch.json"),
        ("UBC-NLP/Casablanca", "casablanca_multidialect.json"),
    ]
    
    results = {}
    
    for dataset_name, output_filename in datasets_to_explore:
        output_path = OUTPUT_DIR / output_filename
        dataset = explore_dataset(dataset_name, output_path)
        results[dataset_name] = dataset is not None
    
    # Summary
    print(f"\n{'='*60}")
    print("Summary")
    print(f"{'='*60}")
    for dataset_name, success in results.items():
        status = "✓" if success else "✗"
        print(f"{status} {dataset_name}")
    
    print(f"\nAll dataset explorations saved to: {OUTPUT_DIR}")
    print("\nNext steps:")
    print("1. Review the saved JSON files to understand dataset structure")
    print("2. Filter for Levantine (Lebanese/Syrian) samples if available")
    print("3. Check for code-switching patterns")
    print("4. Assess audio quality and conditions")


if __name__ == "__main__":
    main()
