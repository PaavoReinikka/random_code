# To save space, I've stuffed every version in one folder:
# Make one version at the time by renaming appropriately
# (or include elsewhere as you like) with naming:
# correlate -> cp, sort -> so, imseg -> is 


bin=pngcorrelate cp-test cp-benchmark
include ../common/Makefile.common
#include ../common/Makefile.cuda

SOURCES+=./../cp-common/*.cc ./../common/*.cc
CXXFLAGS+=-I ./ -I ./../cp-common -I ./../common
vpath %.h ../cp-common:../common
vpath %.cc ../cp-common:../common

pngcorrelate: pngcorrelate.o cp.o pngio.o error.o
	$(CXX) $(LDFLAGS) $^ -lpng -o $@

cp-test: cp-test.o cp.o error.o
	$(CXX) $(LDFLAGS) $^ -o $@

cp-benchmark: cp-benchmark.o cp.o error.o
	$(CXX) $(LDFLAGS) $^ -o $@

# for cuda
#cp.o: cp.cu
#	$(NVCC) $(ALL_CCFLAGS) $(GENCODE_FLAGS) -o $@ -c $<

#pngcorrelate: pngcorrelate.o cp.o pngio.o error.o
#	$(NVCC) $(ALL_LDFLAGS) $(GENCODE_FLAGS) -o $@ $+ -lpng

#cp-test: cp-test.o cp.o error.o
#	$(NVCC) $(ALL_LDFLAGS) $(GENCODE_FLAGS) -o $@ $+

#cp-benchmark: cp-benchmark.o cp.o error.o
#	$(NVCC) $(ALL_LDFLAGS) $(GENCODE_FLAGS) -o $@ $+


include Makefile.dep
