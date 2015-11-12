#!/usr/bin/make -f

.PHONY: all builddatabase gethockeygames

all: builddatabase

builddatabase:
	./hockey15-16.sh

gethockeygames:
	./gethockeygames.sh
