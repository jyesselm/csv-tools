import click
import pandas as pd


@click.command()
@click.option(
    "-i", "--input", required=True, help="input csv(s), seperated by ','",
)
@click.option(
    "-o", "--output", required=False, default="output.csv", help="output csv",
)
@click.option(
    "-a",
    "--add",
    required=False,
    default=None,
    help="columns to add in the format COLNAME1=VAL,COLNAME2=VAL",
)
def main(input, output, add):
    spl = input.split(",")
    dfs = []
    for fname in spl:
        dfs.append(pd.read_csv(fname))
    df = pd.concat(dfs)
    if add is not None:
        spl = add.split()


if __name__ == "__main__":
    main()
