[![Build Status](http://runbot.odoo.com/runbot/badge/flat/1/master.svg)](http://runbot.odoo.com/runbot)
[![Tech Doc](http://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](http://www.odoo.com/documentation/master)
[![Help](http://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](http://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](http://nightly.odoo.com/)

Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>,
<a href="https://www.odoo.com/page/website-builder">Website Builder</a>,
<a href="https://www.odoo.com/page/e-commerce">eCommerce</a>,
<a href="https://www.odoo.com/page/warehouse">Warehouse Management</a>,
<a href="https://www.odoo.com/page/project-management">Project Management</a>,
<a href="https://www.odoo.com/page/accounting">Billing &amp; Accounting</a>,
<a href="https://www.odoo.com/page/point-of-sale">Point of Sale</a>,
<a href="https://www.odoo.com/page/employees">Human Resources</a>,
<a href="https://www.odoo.com/page/lead-automation">Marketing</a>,
<a href="https://www.odoo.com/page/manufacturing">Manufacturing</a>,
<a href="https://www.odoo.com/#apps">...</a>

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.


Getting started with Odoo
-------------------------
For a standard installation please follow the <a href="https://www.odoo.com/documentation/13.0/setup/install.html">Setup instructions</a>
from the documentation.

To learn the software, we recommend the <a href="https://www.odoo.com/slides">Odoo eLearning</a>, or <a href="https://www.odoo.com/page/scale-up-business-game">Scale-up</a>, the <a href="https://www.odoo.com/page/scale-up-business-game">business game</a>. Developers can start with <a href="https://www.odoo.com/documentation/13.0/tutorials.html">the developer tutorials</a>


Developer Guide
---------------
This document is mainly for developers who are first starting working on this project.

**TL;DR**
---------
If you are new, here are something that you should be well aware of:

1. DON’T touch ‘master’ branch (if you’re not the lead developer)
‘master’ branch should only contain the latest working version of the application
2. Write your your commit message descriptively (not ‘my commit’)
3. When creating pull request, write the description well
4. Create a NEW branch for every task assigned to you (not the branch with your name)
5. Each branch should only handle one task
6. Create a gitlab ISSUE for defects found or any request
7. When working on an issue, the branch name should shortly describe the issue (e.g: fix-config-file)
8. DON’T make change to the file that is not relevant to the issue you’re handling

How to make change
------------------
Making changes can be categorised to fixing bugs, fixing typo, adding new features, removing a certain thing, etc. For every change needed to be made a new branch must be created to host that change.

1- Branch out of `develop`
```
git checkout -b [branch-name] develop
```

The above command will create a new branch out of develop branch and switch you to that new branch

Making your first commit
------------------------
Keep in mind that all changes made has to be committed to its corresponding branch.

*Ex: if you fix a typo on the fix-core-module-typo branch then your commit must be pushed to that branch.*

```
git add -A

git commit -m “changing typo on attendance mod”

git push origin fix-core-module-typo
```

How to report bugs / request changes
------------------------------------
For every bug or change request you want to make on the application a Gitlab issue must be created, so other develop can track and know what requests are made and what bugs have been found during the development process. 

```
1. Go to Issue on Gitlab

2. Click `New Issue`

3. Create your issue
```
How to bind your commit to relevant issue
-----------------------------------------
To do so you must take note of the Issue number presented on every issue. (e.g: #12, #4…)

When commiting your change the commit message must specify the issue number the commit belong to
```
git commit -m “test commit #12”
```

How to name your branch
-----------------------
A branch name should describe the task currently working on (NOT YOUR NAME)

```
git branch add-suspension-mod
```