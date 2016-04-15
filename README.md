# Non-Utilitarian Coalition Structure Generation

## Re-creating experiments discsussed in the paper

In order to generate computations on a generic Linux machine please run the following code

```
mkdir build
cd build
cmake ..
make
make problems
make computations
```

Graphs from the paper can be generated with
```
make graphs
```

## File format for MC-Nets representation

Single rule representation:

```
-1 5 5 3 7 2 0 -7 0
```

This rule specifies individual utility of 5 of agent 5, 7 of agent 3, 0 of agent 2 in coalitions where there
  are no agents 1 and 7.

* -1 specifies that agent 1 is in the N-set
* 5 5 specifies that agent 5 is in the P-set and has individual utility 5
* 3 7 specifies that agent 3 is in the P-set and has individual utility 7
* 2 0 specifies that agent 2 is in the P-set and has indivudual utility 0
* -7 specifies that the agent 7 is in the N-set
* 0 represents end of the rule

