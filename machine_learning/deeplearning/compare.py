import argparse
import importlib.util
import sys
import os
import numpy as np
from tests import test_cases

def load_module(file_path):
    module_name = os.path.basename(file_path).replace('.py', '')
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

def run_comparison(problem_file):
    if not os.path.exists(problem_file):
        print(f"Error: File {problem_file} not found.")
        return

    # Extract problem key from filename (e.g., neuralnetworks_fc_forward_high_easy.py -> fc_forward)
    # This might be tricky if naming is loose. Let's rely on the user passing the key or inferring it.
    # Actually, let's just pass the file and let the test runner figure it out or pass the key explicitly.
    
    # For now, let's assume the filename contains the key or we map it.
    # Let's try to map filename to test key.
    filename = os.path.basename(problem_file)
    
    test_key = None
    if 'fc_forward' in filename:
        test_key = 'fc_forward'
    elif 'embedding' in filename:
        test_key = 'embedding'
    elif 'softmax' in filename:
        test_key = 'softmax'
    elif 'cross_entropy' in filename:
        test_key = 'cross_entropy'
    elif 'layer_norm' in filename:
        test_key = 'layer_norm'
    elif 'attention_scaled' in filename:
        test_key = 'scaled_dot_product_attention'
    elif 'rnn_cell' in filename:
        test_key = 'rnn_cell'
    elif 'conv2d_filter' in filename:
        test_key = 'conv2d_filter'
    elif 'fc_backward' in filename:
        test_key = 'fc_backward'
    elif 'pooling' in filename:
        test_key = 'pooling'
    elif 'dropout' in filename:
        test_key = 'dropout'
    elif 'bce' in filename:
        test_key = 'binary_cross_entropy'
    elif 'activations_relu' in filename:
        test_key = 'activations_relu'
    elif 'activations_sigmoid' in filename:
        test_key = 'activations_sigmoid'
    elif 'weight_init' in filename:
        test_key = 'weight_init'
    # Add more mappings as we go
    
    if not test_key:
        print(f"Could not determine test key from filename: {filename}")
        return

    print(f"Loading solution from {problem_file}...")
    try:
        user_module = load_module(problem_file)
    except Exception as e:
        print(f"Failed to load module: {e}")
        return

    print(f"Running tests for: {test_key}")
    if hasattr(test_cases, test_key):
        test_func = getattr(test_cases, test_key)
        try:
            test_func(user_module)
            print("\n✅ All tests passed!")
        except AssertionError as e:
            print(f"\n❌ Test failed: {e}")
        except Exception as e:
            print(f"\n❌ Error during testing: {e}")
            import traceback
            traceback.print_exc()
    else:
        print(f"No tests found for key: {test_key}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare implementation with reference.')
    parser.add_argument('file', help='Path to the implementation file')
    args = parser.parse_args()

    run_comparison(args.file)
