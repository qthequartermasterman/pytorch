import pathlib
from typing import Any, Dict, List, Literal, Optional, Self, Union

import matplotlib
import numpy as np
from _typeshed import Incomplete
from tensorboard.compat.proto.event_pb2 import Event
from tensorboard.summary.writer.event_file_writer import EventFileWriter

import torch

Number = Union[float, int]

class FileWriter:
    event_writer: EventFileWriter
    def __init__(self, log_dir:Union[str, pathlib.Path], max_queue: int = ..., flush_secs: Number = ..., filename_suffix: str = ...) -> None: ...
    def get_logdir(self) -> str: ...
    def add_event(self, event:Event, step: Optional[Number] = None, walltime: Optional[float] = None) -> None: ...
    def add_summary(self, summary:Incomplete, global_step: Optional[Number] = None, walltime: Optional[float] = None) -> None: ...
    def add_graph(self, graph_profile:Incomplete, walltime: Optional[float] = ...) -> None: ...
    def add_onnx_graph(self, graph:Incomplete, walltime: Optional[float] = ...) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...
    def reopen(self) -> None: ...

class SummaryWriter:
    log_dir: str
    purge_step: int
    max_queue: int
    flush_secs: int
    filename_suffix: str
    file_writer: FileWriter
    default_bins: List[Number]
    def __init__(self, log_dir: Optional[str] = ..., comment: str = ..., purge_step: Optional[int] = ..., max_queue: int = ..., flush_secs: int = ..., filename_suffix: str = ...) -> None: ...
    def get_logdir(self)->str: ...
    def add_hparams(self, hparam_dict:Dict[str, Union[bool, str, float, int, None]], metric_dict:Dict[str, Union[bool, str, float, int, None]], hparam_domain_discrete: Optional[Dict[str, List[Any]]] = ..., run_name: Optional[str] = ...) -> None: ...
    def add_scalar(self, tag:str, scalar_value:Union[float, str], global_step: Optional[int] = ..., walltime: Optional[float] = ..., new_style: bool = ..., double_precision: bool = ...) -> None: ...
    def add_scalars(self, main_tag:str, tag_scalar_dict:Dict[str, Union[float,str]], global_step: Optional[int] = ..., walltime: Optional[float] = ...) -> None: ...
    def add_histogram(self, tag:str, values:Union[torch.Tensor, np.ndarray, str], global_step: Optional[int] = ..., bins: Literal['tensorflow', 'auto', 'fd', 'doane', 'scott', 'stone', 'rice', 'sturges', 'sqrt'] = ..., walltime: Optional[float] = ..., max_bins: Optional[int] = ...) -> None: ...
    def add_histogram_raw(self, tag:str, min:Number, max:Number, num: int, sum:Number, sum_squares:Number, bucket_limits:Union[torch.Tensor, np.ndarray], bucket_counts:Union[torch.Tensor, np.ndarray], global_step: Optional[int] = ..., walltime: Optional[float] = ...) -> None: ...
    def add_image(self, tag:str, img_tensor:Union[torch.Tensor, np.ndarray, str], global_step: Optional[int] = ..., walltime: Optional[float] = ..., dataformats: str = ...) -> None: ...
    def add_images(self, tag:str, img_tensor:Union[torch.Tensor, np.ndarray, str], global_step: Optional[int] = ..., walltime: Optional[float] = ..., dataformats: str = ...) -> None: ...
    def add_image_with_boxes(self, tag:str, img_tensor:Union[torch.Tensor, np.ndarray, str], box_tensor:Union[torch.Tensor, np.ndarray, str], global_step: Optional[int] = ..., walltime: Optional[float] = ..., rescale: Number = ..., dataformats: str = ..., labels: Optional[List[str]] = ...) -> None: ...
    def add_figure(self, tag:str, figure:Union[matplotlib.figure.Figure, List[matplotlib.figure.Figure]], global_step: Optional[int] = ..., close: bool = ..., walltime: Optional[float] = ...) -> None: ...
    def add_video(self, tag:str, vid_tensor:torch.Tensor, global_step: Optional[int] = ..., fps: Union[float, int] = ..., walltime: Optional[float] = ...) -> None: ...
    def add_audio(self, tag:str, snd_tensor:torch.Tensor, global_step: Optional[int] = ..., sample_rate: int = ..., walltime: Optional[float] = ...) -> None: ...
    def add_text(self, tag:str, text_string:str, global_step: Optional[int] = ..., walltime: Optional[float] = ...) -> None: ...
    def add_onnx_graph(self, prototxt:Incomplete) -> None: ...
    def add_graph(self, model:torch.nn.Module, input_to_model: Union[torch.Tensor, List[torch.Tensor]] = ..., verbose: bool = ..., use_strict_trace: bool = ...) -> None: ...
    def add_embedding(self, mat:Union[torch.Tensor, np.ndarray], metadata: List[Any] = ..., label_img: Optional[torch.Tensor] = ..., global_step: Optional[int] = ..., tag: str = ..., metadata_header: Incomplete | None = ...) -> None: ...
    def add_pr_curve(self, tag:str, labels:Union[torch.Tensor, np.ndarray, str], predictions:Union[torch.Tensor, np.ndarray, str], global_step: Optional[int] = ..., num_thresholds: int = ..., weights: Incomplete | None = ..., walltime: Optional[float] = ...) -> None: ...
    def add_pr_curve_raw(self, tag:str, true_positive_counts:Union[torch.Tensor, np.ndarray, str], false_positive_counts:Union[torch.Tensor, np.ndarray, str], true_negative_counts:Union[torch.Tensor, np.ndarray, str], false_negative_counts:Union[torch.Tensor, np.ndarray, str], precision:Union[torch.Tensor, np.ndarray, str], recall:Union[torch.Tensor, np.ndarray, str], global_step: Optional[int] = ..., num_thresholds: int = ..., weights: Incomplete | None = ..., walltime: Optional[float] = ...) -> None: ...
    def add_custom_scalars_multilinechart(self, tags:List[str], category: str = ..., title: str = ...) -> None: ...
    def add_custom_scalars_marginchart(self, tags, category: str = ..., title: str = ...) -> None: ...
    def add_custom_scalars(self, layout:Dict[str, Dict[str, List[Union[Literal['Multiline', 'Margin'], List[str]]]]]) -> None: ...
    def add_mesh(self, tag:str, vertices:torch.Tensor, colors: Optional[torch.Tensor] = ..., faces: Optional[torch.Tensor] = ..., config_dict: Optional[Dict[str, Incomplete]] = ..., global_step: Optional[int] = ..., walltime: Optional[float] = ...) -> None: ...
    def flush(self) -> None: ...
    def close(self) -> None: ...
    def __enter__(self:Self) -> Self: ...
    def __exit__(self, exc_type:Any, exc_val:Any, exc_tb:Any) -> None: ...