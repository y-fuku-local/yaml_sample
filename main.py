import argparse
import os
from config import cfg
import logging
import sys
from sample_class import SampleClass

def setup_logger(distributed_rank=0, filename="log.txt"):
    logger = logging.getLogger("Logger")
    logger.setLevel(logging.DEBUG)
    if distributed_rank > 0:
        return logger
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(logging.DEBUG)
    fmt = "[%(asctime)s %(levelname)s %(filename)s line %(lineno)d %(process)d] %(message)s"
    ch.setFormatter(logging.Formatter(fmt))
    logger.addHandler(ch)
    return logger

def get_cfg():
    parser = argparse.ArgumentParser(
        description="parser test"
    )
    parser.add_argument(
        "--cfg",
        default="./sample_param.yaml",
        metavar="FILE",
        help="path to config file",
        type=str,
    )
    args = parser.parse_args()
    cfg.merge_from_file(args.cfg)

    logger = setup_logger(distributed_rank=0)
    logger.info("Loaded configuration file {}".format(args.cfg))
    logger.info("Running with config:\n{}".format(cfg))

    if not os.path.isdir('log'):
        os.makedirs('log')

    with open(os.path.join('log/config.yaml'), 'w') as f:
        f.write("{}".format(cfg))
    return cfg

def main(cfg):
    sample = SampleClass(cfg)
    sample.sender()

if __name__=='__main__':
    main(get_cfg())