import argparse
import json


def main(input, output, type):
    with open(input) as f:
        data = json.load(f)

    for resource in data["resources"]:
        if resource["type"] == type:
            for instance in resource["instances"]:
                name = instance["attributes"]["id"].rsplit(".", 1)[-1]
                instance["index_key"] = name

    with open(output, "w+") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A tutorial of argparse!")
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        type=str,
        help="The path to the old state file as input file",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=True,
        type=str,
        help="The path to the new state file as output file",
    )
    parser.add_argument(
        "-t",
        "--type",
        required=True,
        type=str,
        help="The Terraform type that needs to be converted",
    )
    args = parser.parse_args()

    main(args.input, args.output, args.type)
