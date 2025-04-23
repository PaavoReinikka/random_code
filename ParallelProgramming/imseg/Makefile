# To save space, I've stuffed every version in one folder:
# Make one version at the time by renaming appropriately
# (or include elsewhere as you like) with naming:
# correlate -> cp, sort -> so, imseg -> is 

bin=is-test is-benchmark pngsegment
include ../common/Makefile.common
#include ../common/Makefile.cuda

SOURCES+=./../is-common/*.cc ./../common/*.cc
CXXFLAGS+=-I ./ -I ./../is-common -I ./../common -fopenmp -lpng
LDFLAGS+=-lpng -fopenmp 
vpath %.h ../is-common:../common
vpath %.cc ../is-common:../common

pngsegment: pngsegment.o is.o pngio.o error.o                                                                                                              
	$(CXX) $^ $(LDFLAGS)  -o $@ 

is-test: is-test.o is.o error.o pngio.o
	$(CXX) $^ $(LDFLAGS)  -o $@

is-benchmark: is-benchmark.o is.o error.o
	$(CXX) $(LDFLAGS) $^ -o $@

#is.o: is.cu
#	$(NVCC) $(ALL_CCFLAGS) $(GENCODE_FLAGS) -o $@ -c $<

#pngsegment: pngsegment.o is.o pngio.o error.o
#	$(NVCC) $(ALL_LDFLAGS) $(GENCODE_FLAGS) -o $@ $+ -lpng

#is-test: is-test.o is.o error.o pngio.o
#	$(NVCC) $(ALL_LDFLAGS) $(GENCODE_FLAGS) -o $@ $+ -lpng

#is-benchmark: is-benchmark.o is.o error.o
#	$(NVCC) $(ALL_LDFLAGS) $(GENCODE_FLAGS) -o $@ $+

include Makefile.dep
