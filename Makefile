.PHONY: all
all: ./bin/main

./bin/main: ./src/main.cpp
	g++ --std=c++17 ./src/main.cpp -o ./bin/main

.PHONY: clean
clean:
	rm -f bin/*