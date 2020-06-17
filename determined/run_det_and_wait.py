import argparse
import subprocess
import re

def main():
    parser = argparse.ArgumentParser(description='Run Determined Example')
    parser.add_argument('config', type=str, help='path to experiment config')
    parser.add_argument('context', type=str, help='path to context directory')
    args = parser.parse_args()

    # Submit determined experiment via CLI
    cmd = ["det", "e", "create", args.config, args.context]
    submit = subprocess.run(cmd, capture_output=True)
    output = str(submit.stdout)
    experiment_id = int(re.search("Created experiment (\d+)", output)[1])
    print(f'Created Experiment {experiment_id}')

    # Wait for experiment to complete via CLI
    wait = subprocess.run(["det", "e", "wait", str(experiment_id)])
    print(f"Experiment {experiment_id} completed!")

    # Write experiment id to output file
    with open('/tmp/experiment_id.txt', 'w') as f:
        f.write(str(experiment_id))

if __name__ == '__main__':
    main()
