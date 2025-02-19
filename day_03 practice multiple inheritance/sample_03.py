class mobile:
  def __init__(ad,company,model):
    ad.company=company
    ad.model=model

  def display(ad):
    print(ad.company,ad.model)

while True:
  company = input("Enter the company name (or type 'exit' to stop): ")
  if company.lower() == 'exit':
    break
  model=input("enter the model no:")
  mobile1=mobile(company,model)
  mobile1.display()