from jinja2 import Template

template_text = """
Hello {{ name }}!
{% if age < 13 %}
You are a child.
{% elif age < 18 %}
You are a teenager.
{% else %}
You are an adult.
{%endif%}
"""

temp = Template(template_text)

data = {
    "name":"Ayşe",
    "age": 15,
    }
data2 = {
    "name":"Ahmet",
    "age": 25,
}

data3 = {
    "name":"Feraye",
    "age": 1,
}

output = temp.render(data)
output2 = temp.render(data2)
output3 = temp.render(data3)

print(output)
print(output2)
print(output3)