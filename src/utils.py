"""To run profiling without @profile decorator."""

import logging

from line_profiler import LineProfiler

logging.basicConfig(level=logging.INFO)


def profiler(f, *args):
    """Allows to pass functions to profile in command line.

    This removes the need to comment and uncomment @profile
    """
    # parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     "function",
    #     help="name of the functions where decorators will be used",
    #     type=str,
    #     nargs="+",  # allowing multiple arguments
    # )
    # argument = parser.parse_args()
    # logging.info(f"{argument.function}")

    lp = LineProfiler()
    f_wrapped = lp(f)
    f_wrapped(*args)
    lp.print_stats()
