# Knowledge Graph Embedding Semantics

Vocabulary for investigating whether knowledge graph embeddings capture the semantics of the FB15k-237 and YAGO3-10 knowledge graphs.

## Graph

**Triple**:
A directed fact (head entity, relation, tail entity) in a knowledge graph.
_Avoid_: Edge, fact, statement

**Entity**:
A node of the knowledge graph that appears as the head or tail of at least one triple.
_Avoid_: Node, vertex, object

**Relation**:
A labeled kind of directed link that connects a head entity to a tail entity.
_Avoid_: Predicate, property, edge type

**Self-loop**:
A triple whose head entity and tail entity are the same entity.

## Semantics

**Class**:
A semantic category that an entity belongs to, such as Person or City. An entity can belong to more than one class.
_Avoid_: Type, category, label

**Level**:
The depth of a class in the WordNet-based class hierarchy, counted from the coarse top classes (level 1: person, organization, body of water, product) downwards.

**Profile**:
The set of (direction, relation) pairs an entity takes part in. It is a structural signature and is not a class.
_Avoid_: Signature, type

## Evaluation

**Experiment**:
A named set of sibling classes at one level, evaluated together, e.g. Level-2-Persons (artist, officeholder, writer, scientist, politician).
_Avoid_: Task, class set

**Run**:
One evaluation of one experiment with one embedding model and one classifier or clustering algorithm.
_Avoid_: Experiment, trial

## Splits

**Triple split**:
The official partition of a dataset's triples into train, valid and test, used to train and evaluate embeddings.
_Avoid_: Dataset split, data split

**Entity split**:
The 80/20 partition of labeled entities into train and test, used to evaluate class prediction from embeddings.
_Avoid_: Classification split, data split
