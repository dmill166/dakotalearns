---
date: 2023-02-06
slug: entity-relationship-diagrams
tags:
  - Attribute
  - Business Requirements
  - Chen
  - Chen Notation
  - Database
  - Diagram
  - Draw.io
  - Entity
  - Entity-Relationship
  - ER Diagram
  - LucidChart
  - Model
  - Relationship
categories:
  - Tutorials
---

# Entity Relationship Diagrams

Oh, hello there. I'm glad you found your way back to my blog!

<!-- more -->

I want to discuss a topic from my [CS 6400: Database Systems Concepts and Design](https://omscs.gatech.edu/cs-6400-database-systems-concepts-and-design) course I'm currently enrolled in at Georgia Institute of Technology (as part of their [OMSCS](https://omscs.gatech.edu/home) program).

1. [What is it?](https://dakotalearns.wordpress.com/2023/02/05/entity-relationship-diagrams/#what-is-it)
2. [Terminology](https://dakotalearns.wordpress.com/2023/02/05/entity-relationship-diagrams/#terminology)
3. [Guides to Using It](https://dakotalearns.wordpress.com/2023/02/05/entity-relationship-diagrams/#guides-to-using-it)
4. [Summary and Links](https://dakotalearns.wordpress.com/2023/02/05/entity-relationship-diagrams/#summary-and-links)
5. [Conclusion](https://dakotalearns.wordpress.com/2023/02/05/entity-relationship-diagrams/#conclusion)

## What is it?

From a business standpoint, it can be daunting to think about how to talk to your IT/technical teams to request a database implementation or modifications. The ER (Entity-Relationship) model presents a high-level overview where you can illustrate your business needs in a concise and [relatively] universal way that specifies requirements well for their development efforts.

Peter Chen is credited with developing ER modeling in the 1970s (per [LucidChart](https://www.lucidchart.com/pages/er-diagrams)). You may see "Chen's notation" as an option in various modelling tools considering this fact.

![](https://dakotalearns.wordpress.com/wp-content/uploads/2023/02/image.png?w=680)

[GitMind Illustration of ER Diagram](https://www.google.com/url?sa=i&url=https%3A%2F%2Fgitmind.com%2Ferd-examples.html&psig=AOvVaw3LAwMS5QUQ1nvLDdKT5o2b&ust=1675707298267000&source=images&cd=vfe&ved=0CAMQjB1qFwoTCJjcgaT-_vwCFQAAAAAdAAAAABAE)

Using the above illustration as a starting point, you can start to see the business value in knowing how to create these. A medical office may have information it wants to keep on doctors such as their specializations. In addition, those doctors will have patients they see on some frequency; ideally, those patients have insurance and, likely, those patients have some type of diagnoses. Although this is only a small subset of the type of information that can be outlined, I hope this illustrates the value to you (regardless of your role in your organization).

## Terminology

I mentioned earlier there was some [relatively] universal methods for communicating ER diagrams to others (so that we're designing them the same way across industries and around the world). This graphic below details the most common elements:

![](https://dakotalearns.wordpress.com/wp-content/uploads/2023/02/image-1.png?w=408)

[SQL Server Mentalist Graphic of ER Diagram Elements](https://sqlmentalist.com/2013/10/13/bisql-laymen-to-sql-developer-23-entity-relationship-model-2-er-model-concept-with-an-example/)

* Entity: These are the building blocks of your diagram. Central elements, these are the "things" you care most about and will want to describe and relate to other things
* Weak Entity: These are "pretty" or "extra" things. They rely on Entities (also called Strong Entities) in order to exist. If you removed the Strong Entity they're associated with, they can't stand on their own as a diagrammed element
* Relationship: These are the ropes tying Entities together. They show how two entities are related to one another
* Identifying Relationship: These are the strings tying a weak Entity to a strong Entity. Again, without the Strong Entity, these cannot exist on their own
* Attribute: These are the properties of your "things", or how you describe those things
* Key Attribute: This/These are the unique property(ies) that differentiate one "thing" from another "thing"
* Multi-valued: These are special cases of an Attribute that can have multiple values present to describe a single "Thing" (rather than the normal, atomic nature of Attributes being single-valued)
* Composite Attribute: These are ways to describe a thing that can be broken down into even smaller components (in those cases, the smaller pieces are called Component Attributes)
* Derived Attribute: This is a special type of Attribute that requires calculation or derivation from another attribute or set of attributes
* Total Participation: Symbolized by the double lines, this represents that each of the attached entities MUST participate in the relationship (if this isn't required, a single-line is used and this may be referred to as "partial participation")
* Cardinality Ratio: This is the number of "things" from a specific entity that are related to another number of "things" from another specific entity
* Structural Constraint: This is a more specific Cardinality Ratio (using specific numbers to represent the minimum and maximum participation in the Relationship)

## Guides to Using It

Great - I've thrown a bunch of pictures and terminology at you! But how can you possible use this? Don't worry, just sit there and buckle up as I walk you through an example.

![](https://dakotalearns.wordpress.com/wp-content/uploads/2023/02/image-2.png?w=640)

[Sample ER Diagram](https://www.google.com/url?sa=i&url=https%3A%2F%2Fcodeandwork.github.io%2Fcourses%2Fcs%2FsqlErdSimpleQueries.html&psig=AOvVaw2qVx0i0piW_BXHB7DsSq2l&ust=1675708194674000&source=images&cd=vfe&ved=0CAMQjB1qFwoTCIiVs8-B__wCFQAAAAAdAAAAABAt)

* Entity: In this diagram, we have two entities: Employee and Project.
  + An Employee has two Attributes, a Salary (likely a whole number or decimal number limited to two decimal places) and a Name (the Name is a Composite Attribute, broken down further into two Component Attributes: First Name and Last Name). Not shown here are other attributes we could show for the Employee such as their job title and the Employee ID of their supervisor
  + A Project has no Attributes shown, but we can imagine it likely has an ID identifying the project, a name for the project, a start date, and a description of what the project will accomplish
* Weak Entity: In this diagram, Dependent is a Weak Entity. An Employee (strong entity) at a company may carry some form of benefits and, through these benefits, ensure a number of dependents. Without the employee's employment at the company, the dependents could not exist (in a benefit-sharing capacity), so this is considered a Weak Entity (dependent on the existence of Employee)
* Relationship: The Employee and Project entities are connected through the Assigned-To Relationship. This can be read as "Employees are assigned to a Project". I'll discuss below in the Cardinality Ratio the significate of the m and n represented along this relationship
  + Another detail to call out is the existence of an Attribute on this Relationship, Project Role. Employees may have various roles across various projects (Contributor, Manager, Stakeholder, etc), so this Attribute allows clarification of Employees and their stake in the specific Project
* Identifying Relationship: The Emp-Dep Identifying Relationship shows the connection between Employees and Dependents. We can imagine that Dependent records likely have an attribute identifying to which Employee they are associated (as part of this Relationship)
* Attribute: Called out throughout the above explanations, these are the ovals such as Salary, First Name, or Project Role. They can be associated with Entities (strong or weak) as well as Relationships
* Key Attribute: An identifying attribute to separate instances of the Entity, this could be the Employee ID (unique to their employment at this job) or Project ID (specific to a single Project at a given point in time)
* Multi-valued: There aren't any multi-valued attributes in this diagram, but we could add one (a double-line oval) to the Projects if we wished and name it "Categories". We could store the benefits for the company through accomplishment of this Project and allow multiple category assignment (such as "Operational" and "Financial" if it impacts the company in both of these ways)
* Composite Attribute: In this diagram, the Employee Entity has a Name attribute; this is a Composite attribute. We can see this as it's broken down further into it's Component Attributes, First Name and Last Name
* Derived Attribute: In this diagram, we don't have any Derived Attributes pictured. An example of this would be a "CurrentAge" Attribute on Employee. This would update daily based on their DateOfBirth and store only a whole number year (such as 34). It is Derived because we require the DateOfBirth Attribute to be present in order to have values produced for this Attribute for each Entity
* Total Participation: Not pictured in this diagram, we could make the line connecting Emp-Dep and Dependent a double-line to illustrate total participation. We could do this because each dependent must "belong" to some Employee Entity, so all Dependents will map to some Employee
* Cardinality Ratio: First discussing the Employee and Project relationship with the ratio "n" and "m" shown... this is a "many-to-many" relationship meaning "An employee can be assigned to any number of projects and a project can have any number of employees assigned to it". There are no minimums and multiples may exist in each direction (a single project may have many employees assigned and a single employee may be assigned to many projects). Next, looking at the Employee and Dependent relationship, we have "1" and "n". This is a "one-to-many" relationship. This means that one employee can have many dependents and many dependents may "belong" to the same employee entity. Not pictured here is a "one-to-one" cardinality which is self-described; one entity from one side of the relationship corresponds to one entity from the other side of the relationship
* Structural Constraint: Not illustrated in this diagram, a structural constraint could specify something like (0, 4) for the Emp-Dep Relationship, meaning that an Employee is allowed to have no Dependents associated with them all the way up to a maximum of four dependents associated with them

## Summary and Links

ER Diagrams are a way to communicate a desired database design in a high-level fashion. From a business standpoint, constraints of the real world can be illustrated diagrammatically and allow communication between non-technical and technical teams with the use of an ERD.

If you want a more thorough dive into ER Diagrams, check out the LucidChart link below. I find it to be an excellent resource covering multiple facets of Entity-Relationship Diagrams.

* [Course Description for CS 6400 @ Georgia Tech OMSCS](https://omscs.gatech.edu/cs-6400-database-systems-concepts-and-design)
* [Home Page for OMSCS Program](https://omscs.gatech.edu/home)
* [LucidChart Reference on ER Diagrams](https://www.lucidchart.com/pages/er-diagrams)
* [GitMind Illustration of ER Diagram](https://www.google.com/url?sa=i&url=https%3A%2F%2Fgitmind.com%2Ferd-examples.html&psig=AOvVaw3LAwMS5QUQ1nvLDdKT5o2b&ust=1675707298267000&source=images&cd=vfe&ved=0CAMQjB1qFwoTCJjcgaT-_vwCFQAAAAAdAAAAABAE)
* [SQL Server Mentalist Graphic of ER Diagram Elements](https://sqlmentalist.com/2013/10/13/bisql-laymen-to-sql-developer-23-entity-relationship-model-2-er-model-concept-with-an-example/)
* [Sample ER Diagram](https://www.google.com/url?sa=i&url=https%3A%2F%2Fcodeandwork.github.io%2Fcourses%2Fcs%2FsqlErdSimpleQueries.html&psig=AOvVaw2qVx0i0piW_BXHB7DsSq2l&ust=1675708194674000&source=images&cd=vfe&ved=0CAMQjB1qFwoTCIiVs8-B__wCFQAAAAAdAAAAABAt)

## Conclusion

Rather than diving into a technical feature for the purpose of pushing out an article (and only do a half-decent job), I wanted to talk about something I've had a lot of exposure to recently (thanks to my Master's program) and felt confident discussing. Admittedly, I haven't seen a lot of application for ER diagrams in the roles I've held. A more usable diagram for my purposes has been the Relational Model (maybe a future blog post topic!).

Thanks for taking the time to read this post. Until the next time we learn (or discuss) something together, have a wonderful Monday!
