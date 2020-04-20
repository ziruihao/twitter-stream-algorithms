from twitter_stream import TwitterStream
from shakespeare_stream import ShakespeareStream
from streaming_algorithms import MisraGries
from streaming_algorithms import Exact
from streaming_algorithms import MorrisCounter
from streaming_algorithms import CountSketch
from streaming_algorithms import BJKST
import time
import sys
import os

success = False

while(not success):
    # try:
    stamp = str(int(time.time()) % 10000)

    source = input('Data source: Twitter or Shakespeare? [twitter / shakespeare]: ')

    twitter_mode = ''

    if (source == 'twitter'):
        twitter_mode = input('Twitter data type [hashtags / body_text / locations]: ')
    elif (source != 'shakespeare'):
        print('Error: bad input')
        continue

    algorithm_choice = input('Algorithm choice:\n\t[1] Moris - total tokens\n\t[2] BJKST - total distinct tokens\n\t[3] Misra-Gries - token frequencies\n\tCountSketch - token frequencies (under construction)\nSelection:')

    limit = int(input('Stream token limit (when do we stop, [int]): ')
)
    algorithms = [Exact()]

    if (algorithm_choice == '1'):
        t = int(input('Number of parallel Moris estimators for median computation [int > 0]: '))
        algorithms.append(MorrisCounter(t=t))
    elif (algorithm_choice == '2'):
        k = int(input('BJKST bin size (how many tokens do we cache at a time (substantially smaller than limit, but > 10): '))
        t = int(input('Number of parallel BJKST estimators for median computation [int > 0]: '))
        algorithms.append(BJKST(k=k, t=t))
    elif (algorithm_choice == '3'):
        k = int(input('Misra-Gries bin count (how many counts do we cache at a time (substantially smaller than limit, but > 10): '))
        algorithms.append(MisraGries(k=k, scoring_method='sequence_match'))
    elif (algorithm_choice == '123'):
        algorithms.append(MorrisCounter(t=500))
        algorithms.append(BJKST(k=10, t=500))
        algorithms.append(MisraGries(k=10, scoring_method='sequence_match'))

    else:
        print('Error: bad input')
        continue

    # algorithms.append(CountSketch(k=100, t=500))

    input('< Press Enter to being streaming >')

    stream = {}

    if (source == 'twitter'):
        stream = TwitterStream(limit=limit, algorithms=algorithms)
        stream.set_mode(twitter_mode)
        stream.set_filter(['covid'])
    elif (source == 'shakespeare'):
        stream = ShakespeareStream(limit=limit, algorithms=algorithms)
        stream.stream('shakespeare')

    print('\nFinished!\n')

    for algorithm in algorithms:
        algorithm.query_all(stamp)

    success = True
    
    # except:
    #     continue