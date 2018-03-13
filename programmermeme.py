class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print('%s goes to work.' % self.name)


class Employee(Person):
    def __init__(self, name, age, job):
        super(Employee, self).__init__(name, age)
        self.job = job

    def work(self):
        if self.job[0] == 'a' or 'e' or 'i' or 'o' or 'u':
            print('%s goes to work as an %s' % (self.name, self.job))
        else:
            print('%s goes to work as a %s' % (self.name, self.job))


class Programmer(Employee):
    def __init__(self, name, age, job, language):
        super(Programmer, self).__init__(name, age, 'Programmer')
        self.language = language

    def work(self):
        print('%s goes to work to program in %s' % (self.name, self.language))
