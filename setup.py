from setuptools import setup, find_packages

setup(
    name='yt-app',
    version='0.1',
    packages=find_packages(
        include=["db*", "workers*", "mock*"]    
    ),
    entry_points='''
        [console_scripts]
        video_aggregation_worker=workers.video_aggregation_worker.worker:main
    '''
)