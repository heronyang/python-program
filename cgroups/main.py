import os
import subprocess

from cgroups import Cgroup

# First we create the cgroup 'app' and we set it's cpu and memory limits
cg = Cgroup('app')
cg.set_cpu_limit(50)
cg.set_memory_limit(500)

# Then we a create a function to add a process in the cgroup
def in_my_cgroup():
    pid  = os.getpid()
    cg = Cgroup('app')
    cg.add(pid)

# And we pass this function to the preexec_fn parameter of the subprocess call
# in order to add the process to the cgroup
p1 = subprocess.Popen(['p1'], preexec_fn=in_my_cgroup)
p2 = subprocess.Popen(['p2'], preexec_fn=in_my_cgroup)
p3 = subprocess.Popen(['p3'], preexec_fn=in_my_cgroup)

# Processes worker_1, worker_2, and worker_3 are now in the cgroup 'app'
# and all limits of this cgroup apply to them

# We can change the cgroup limit while those process are still running
# cg.set_cpu_limit(80)

# And of course we can add other applications to the cgroup
# Let's say we have an application running with pid 27033
# cg.add(27033)
