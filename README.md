CrowdComputing
==============

Distributed Edison computational network

This web-app and corresponding python suite will allow you to access the full potential of your new Intel Edison board, by tapping in to the unused potential of other users. Each board on the network has been volunteered to offer computational space and time to the collective, in exchange for the same privilidge. The concept is simple:

You add the software to your board, and sign up for the service. This connects your board to a network of other boards willing to share computational power. 

You grab a cluster of nodes. This can be private clusters of your own boards, or globally-sourced clusters of nearby available boards.

You submit a job. Jobs are essentially segmentable data, combined with a python mapping and reducing script. The data will be "Mapped" out to the boards in your cluster via the mapping script, then the reducer script will be run on the subset of data belonging to each board. This allows for very large jobs to be done on these tiny machines.

After each board completes, the data is returned to the server for storage, and is compiled in to an output file. This finished file is stored on the server, and should represent the output of each board's job.

This concept is modelled after Hadoop's Map-Reduce, but on a smalled data scale to deal with the limited storage of the device. Instead, this model focuses on increasing processing power, allowing faster completion of VERY large jobs.

Example: List sort

A word list such as all the words in "War and Peace" needs to be sorted. The list of words would overflow a single Edison's memory, but that's why we are here!

data: War\_and_Peace.txt
mapper: create list of words, separated by first letter -> 26 lists at amuch smaller size each
reducer: sort each list

The job would send 26 "blocks" to some number of Edison boards, and each block would be sorted independently. Then the Edisons would send the data back in block order. sorted A list + sorted B list + ... + sorted z list = sorted list!

In this way, we can multiply the Edison board's computational power to unthinkable heights!
