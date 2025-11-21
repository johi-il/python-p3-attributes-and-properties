#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name=None,job=None):
        if job is not None:
            self.job=job
        if name is not None:
            self.name=name


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if isinstance(name,str) and (len(name)>=1 and len(name)<=25):
            self._name=name.title()
        else:
            self._name=None
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job
    @job.setter
    def job(self,job):
        if job in APPROVED_JOBS:
            self._job=job
        else:
            self._job=None
            print("Job must be in list of approved jobs.")
    pass
