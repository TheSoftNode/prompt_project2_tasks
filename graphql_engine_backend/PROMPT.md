# Hasura GraphQL Engine Backend Architecture Analysis

**Subdomain:** Code Repo Documentation

---

Your goal is to investigate the hasura/graphql-engine GitHub repository and complete the following tasks regarding its content. Reference the most recent commit as of February 6, 2026.

**Question 1: Paper and Design References**
The repository's architecture documentation at `server/documentation/deep-dives/multiple-backends-architecture.md` directly cites a seminal academic paper that inspired the Backend type class design. Identify the title and first author of that paper. Additionally, identify the title and first author of the seminal paper that formally established the semantics of the GraphQL query language — the query language that the Hasura GraphQL Engine implements — as referenced in the source code comments throughout `server/src-lib/` (e.g., `spec.graphql.org/June2018`).

**Question 2: Backend Type Class Architecture**
The architecture documentation states that a specific total number of typeclasses are required for a new backend to be supported, and lists them by name. Identify that count and list the names of all five typeclasses. Then, list the names of all data constructors defined in the `BackendTag` GADT in `server/src-lib/Hasura/RQL/Types/BackendTag.hs`, in the order they appear in the source file.

**Question 3: AnyBackend Dispatch Functions**
The `server/src-lib/Hasura/SQL/AnyBackend.hs` module provides dispatch functions for working with existentially-typed backend values. Identify the name of the type constraint alias defined with the signature `type ... (c :: BackendType -> Constraint) =` that generates constraints for all backends simultaneously. Then list all exported function names from this module that begin with the prefix `dispatch`, in the order they appear in the module's export list.

**Question 4: Extension Types Pattern**
The Backend type class uses an extension type mechanism where setting `XRelay 'MSSQL = Void` makes certain IR constructors unrepresentable at compile time. In `server/src-lib/Hasura/RQL/IR/Select.hs`, identify the exact constructor name in the `AnnFieldG` data type that takes `(XRelay b)` as its first argument. Then identify the full Haskell type name of the second argument to that same constructor (the argument immediately after `XRelay b`).

**Question 5: Backend Implementation Comparison Table**
Create a table with exactly 3 rows and 4 columns comparing three Backend type class instances. The table must have four columns showing: (1) the backend name as it appears in the `BackendTag` GADT constructor without the "Tag" suffix (e.g., "PostgresVanilla"), (2) the file path of the Backend instance definition relative to `server/src-lib/` (e.g., `Hasura/Backends/Postgres/Instances/Types.hs`), (3) the value assigned to `XRelay` for that backend (`XEnable`, `XDisable`, or `Void`), and (4) the value returned by `namingConventionSupport` for that backend (`AllConventions` or `OnlyHasuraCase`). The three backends to compare are Postgres Vanilla, MSSQL, and BigQuery.

## Citations

[1] hasura/graphql-engine. "Multiple Backends Architecture Documentation." _server/documentation/deep-dives/multiple-backends-architecture.md_, commit 8d63a1ff726e4fddf8324f259400393467d8021d. GitHub. https://github.com/hasura/graphql-engine/blob/8d63a1ff726e4fddf8324f259400393467d8021d/server/documentation/deep-dives/multiple-backends-architecture.md

[2] Najd, S., & Jones, S. P. (2017). Trees That Grow. _Journal of Universal Computer Science_, 23(1), 42–62. https://arxiv.org/abs/1610.04799

[3] Hartig, O., & Pérez, J. (2018). Semantics and Complexity of GraphQL. In _Proceedings of the 2018 World Wide Web Conference_ (WWW '18), pp. 1155–1164. ACM. https://doi.org/10.1145/3178876.3186014

[4] hasura/graphql-engine. "BackendTag GADT Definition." _server/src-lib/Hasura/RQL/Types/BackendTag.hs_, commit 8d63a1ff726e4fddf8324f259400393467d8021d. GitHub. https://github.com/hasura/graphql-engine/blob/8d63a1ff726e4fddf8324f259400393467d8021d/server/src-lib/Hasura/RQL/Types/BackendTag.hs

[5] hasura/graphql-engine. "AnyBackend Existential Container." _server/src-lib/Hasura/SQL/AnyBackend.hs_, commit 8d63a1ff726e4fddf8324f259400393467d8021d. GitHub. https://github.com/hasura/graphql-engine/blob/8d63a1ff726e4fddf8324f259400393467d8021d/server/src-lib/Hasura/SQL/AnyBackend.hs

[6] hasura/graphql-engine. "IR Select Types." _server/src-lib/Hasura/RQL/IR/Select.hs_, commit 8d63a1ff726e4fddf8324f259400393467d8021d. GitHub. https://github.com/hasura/graphql-engine/blob/8d63a1ff726e4fddf8324f259400393467d8021d/server/src-lib/Hasura/RQL/IR/Select.hs

[7] hasura/graphql-engine. "Postgres Backend Instance." _server/src-lib/Hasura/Backends/Postgres/Instances/Types.hs_, commit 8d63a1ff726e4fddf8324f259400393467d8021d. GitHub. https://github.com/hasura/graphql-engine/blob/8d63a1ff726e4fddf8324f259400393467d8021d/server/src-lib/Hasura/Backends/Postgres/Instances/Types.hs

[8] hasura/graphql-engine. "MSSQL Backend Instance." _server/src-lib/Hasura/Backends/MSSQL/Instances/Types.hs_, commit 8d63a1ff726e4fddf8324f259400393467d8021d. GitHub. https://github.com/hasura/graphql-engine/blob/8d63a1ff726e4fddf8324f259400393467d8021d/server/src-lib/Hasura/Backends/MSSQL/Instances/Types.hs

[9] hasura/graphql-engine. "BigQuery Backend Instance." _server/src-lib/Hasura/Backends/BigQuery/Instances/Types.hs_, commit 8d63a1ff726e4fddf8324f259400393467d8021d. GitHub. https://github.com/hasura/graphql-engine/blob/8d63a1ff726e4fddf8324f259400393467d8021d/server/src-lib/Hasura/Backends/BigQuery/Instances/Types.hs
