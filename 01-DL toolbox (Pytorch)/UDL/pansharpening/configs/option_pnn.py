import argparse
# from UDL.Basis.option import panshaprening_cfg, Config, os
from UDL.AutoDL import TaskDispatcher
import os

class parser_args(TaskDispatcher, name='PNN'):
    def __init__(self, cfg=None):
        if cfg is None:
            from UDL.Basis.option import panshaprening_cfg
            cfg = panshaprening_cfg()

        script_path = os.path.dirname(os.path.dirname(__file__))
        root_dir = script_path.split(cfg.task)[0].replace('\\', '/')

        model_path = f'/home/woo/文档/GitHub/UDL_bak/UDL/results/pansharpening/wv3/PNN/Test/model_2022-04-26-16-16-20/11990.pth.tar'
        # model_path = f'/home/woo/文档/GitHub/UDL_bak/UDL/results/pansharpening/qb/PNN/Test/model_2022-04-27-01-23-00/11990.pth.tar'
        # model_path = f'/home/woo/文档/GitHub/UDL_bak/UDL/results/pansharpening/gf2/PNN/Test/11998.pth.tar'

        parser = argparse.ArgumentParser(description='PyTorch Pansharpening Training')
        # * Logger
        parser.add_argument('--out_dir', metavar='DIR', default=f'{root_dir}/results/{cfg.task}',
                            help='path to save model')
        # * Training
        parser.add_argument('--lr', default=1e-3, type=float)  # 1e-4 2e-4 8
        parser.add_argument('--lr_scheduler', default=True, type=bool)
        parser.add_argument('--samples_per_gpu', default=64, type=int,  # 8
                            metavar='N', help='mini-batch size (default: 256)')
        parser.add_argument('--print-freq', '-p', default=500, type=int,
                            metavar='N', help='print frequency (default: 10)')
        parser.add_argument('--seed', default=1, type=int,
                            help='seed for initializing training. ')
        parser.add_argument('--epochs', default=12000, type=int)
        parser.add_argument('--workers_per_gpu', default=0, type=int)
        parser.add_argument('--resume_from',
                            default=model_path,
                            type=str, metavar='PATH',
                            help='path to latest checkpoint (default: none)')
        # * Model and Dataset
        parser.add_argument('--arch', '-a', metavar='ARCH', default='PNN', type=str,
                            choices=['PanNet', 'DiCNN', 'PNN', 'FusionNet'])
        parser.add_argument('--dataset', default={'train': 'wv3', 'val': 'wv3_multiExm.h5'}, type=str,
                            choices=[None, 'wv2', 'wv3', 'wv4', 'qb', 'gf',
                                     'wv2_hp', ...,
                                     'fr', 'wv3_singleMat', 'wv3_multi_exm1258', 'wv3_OrigScale_multiExm1.h5'],
                            help="performing evalution for patch2entire")
        parser.add_argument('--eval', default=False, type=bool,
                            help="performing evalution for patch2entire")
        args = parser.parse_args()
        args.start_epoch = args.best_epoch = 1
        args.experimental_desc = 'Test'
        cfg.merge_args2cfg(args)
        cfg.workflow = [('train', 1)]
        cfg.img_range = 2047.0
        print(cfg.pretty_text)
        self._cfg_dict = cfg