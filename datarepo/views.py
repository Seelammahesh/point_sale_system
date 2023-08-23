from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Category, SubCategory, Product

from rest_framework.response import Response
from django.core.exceptions import ViewDoesNotExist


# Create your views here.
@api_view(['POST'])
def add_category(request):
    name = request.POST.get('name', None)
    if name is None:
        context = {
            'message': "Name is Missing"
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_name = Category.objects.create(name=name)
            new_name.save()
            context = {
                'message': 'Sucessfully Added NewCategory',
                'data': {
                    'category_id': new_name.id,
                    'name': new_name.name
                }
            }
            return Response(context, status=status.HTTP_201_CREATED)

        except Category.DoesNotExist:
            context ={
                'message':'Invalid Name'

            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            context = {
                'message': "invalid Name"
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_category(request):
    list_categories = Category.objects.all()
    category_data = []
    for category in list_categories:
        data = {
            'category_id': category.id,
            'category_name': category.name
        }
        category_data.append(data)

    context ={
        'category_data':category_data
        }
    return Response( context,status=status.HTTP_200_OK)



@api_view(['PATCH'])
def update_category(request):
    category_id = request.POST.get('category_id',None)
    new_name = request.POST.get('name',None)
    if category_id is None:
        context={
            'message':'Category_id is Missing'

        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_category = Category.objects.get(id=category_id)
            get_category.name = new_name if new_name is not None else get_category.name
            get_category.save()
            context ={
                'message':"Category Updated Successfully"
            }
            return Response(context,status=status.HTTP_200_OK)

        except ValueError:
            context ={
                'message':'Invalid Category_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_category(request):
    category_id = request.POST.get('category_id',None)
    if category_id is None:
        context ={
            'message':'Category_id is Missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_category=Category.objects.get(id=category_id)
            get_category.delete()
            context ={
                'message':'Category_id Sucessfully Deleted'
            }
            return Response(context,status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            context={
                'message':'Invalid Category_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

        except ValueError:
            context ={
                'message':'Invalid Category_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_subcategory(request):
    category_id = request.POST.get('category_id',None)
    name=request.POST.get('name',None)

    if category_id is None:
        context={
            'message':'Category ID is Missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            category=Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            context ={
                'message':'Invalid Category_ID'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        if name is None:
            context ={
                'message':'Name is Missing'

            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                new_subcategory=SubCategory.objects.create(
                    category=category,name=name
                )
                new_subcategory.save()
                context ={
                    'message':'New Subcategory Added SuccessFully',
                    'date':{
                    'subcategory_id':new_subcategory.id,
                    'category_id':category_id,
                    'name':new_subcategory.name
                }
                }
                return Response(context,status=status.HTTP_201_CREATED)
            except ValueError:
                context ={
                    'message': 'Invalid Name'
                }
                return  Response(context,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def list_subcategory(request):
    all_subcategories = SubCategory.objects.all()
    subcategories = []
    for subcategory in all_subcategories:
        temp = {
            'subcategory_id': subcategory.id,
            'subcategory_name': subcategory.name
        }
        subcategories.append(temp)
        context = {
            'subcategories': subcategories
        }
        return Response(context, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update_subcategory(request):
    subcategory_id=request.POST.get('subcategory_id',None)
    new_name=request.POST.get('new_name',None)
    if subcategory_id is None:
        context ={
            'message':'Subcategory_ID is Missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_subcategory = SubCategory.objects.get(id=subcategory_id)
            get_subcategory.name=new_name if new_name is None else get_subcategory.name
            get_subcategory.save()
            context ={
                'message':"Subcategory Updated SuccessFully"
            }
            return Response(context,status=status.HTTP_200_OK)

        except SubCategory.DoesNotExist:
            context ={
                'message':'Invalid Subcategory_ID'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            context ={
                'message': 'Invalid Subcategory_ID'
            }
            return  Response(context,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_subcategory(request):
    subcategory_id=request.POST.get('subcategory_id',None)
    if subcategory_id is None:
        context ={
            'message':'Subcategory_ID is Missing'
        }
    else:
        try:
            get_subcategory=SubCategory.objects.get(id=subcategory_id)
            get_subcategory.delete()
            context ={
                'message':'Subcategory SuccessFully deleted '
            }
            return Response(context,status=status.HTTP_200_OK)
        except SubCategory.DoesNotExist:
            context ={
                'message':'Invalid Sucategory_ID'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            context={
                'message':'Invalid Subcategory_ID'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_product(request):
    subcategory_id=request.POST.get('subcategory_id',None)
    name=request.POST.get('name',None)
    price=request.POST.get('price',None)
    description= request.POST.get('description',None)
    if subcategory_id is None or name is None or price is None or description is None:
        context ={
            'message':'subcategory_id/name/price/description is missing Please check.'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_product=Product.objects.create(
                sub_category_id=subcategory_id,
                name=name,
                price=price,
                description=description

            )
            new_product.save()
            context={
                'message':'Product Added SuccessFully',
                'data':{
                    'product_id':new_product.id,
                    'sub_category_id':new_product.sub_category.id,
                    'subcategory_name':new_product.sub_category.name,
                    'product_name':new_product.name,
                    'price':new_product.price,
                    'description':new_product.description,
                    'created_on':new_product.created_on,
                    'updated_on':new_product.updated_on

                }
            }
            return  Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context ={
                'message':'Invalid Product'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_products(request):
    all_products = Product.objects.all()
    products = []

    for product in all_products:
        subcategory_name = product.sub_category.name if product.sub_category else None

        temp = {
            'subcategory_id': product.sub_category_id,
            'subcategory_name': subcategory_name,
            'name': product.name,
            'price': product.price,
            'description': product.description
        }
        products.append(temp)

    context = {
        'products': products
    }

    return Response(context, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update_product(request):
    product_id =request.POST.get('product_id',None)
    if product_id is None:
        context ={
            'message':'Product_ID is Missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_product =Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            context ={
                'message':'Product Not Found'

            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

        subcategory_id=request.POST.get('subcategory_id',Product.sub_category_id)
        name=request.POST.get('name',Product.name)
        price=request.POST.get('price',Product.price)
        description=request.POST.get('description',Product.description)

        new_product.sub_category_id = subcategory_id
        new_product.name = name
        new_product.price = price
        new_product.description = description
        new_product.save()



        context = {
            'message': 'Product updated successfully',
            'data': {
                'product_id': new_product.id,
                'subcategory_id': new_product.sub_category_id,
                'name': new_product.name,
                'price': new_product.price,
                'description': new_product.description,
                'created_on': new_product.created_on,
                'updated_on': new_product.updated_on
            }
        }
        return Response(context, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_product(request):
    product_id =request.POST.get('product_id')
    if product_id is None:
        context ={
            'message':'Product is Missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            to_delete_product_id=Product.objects.get(id=product_id)
            to_delete_product_id.delete()
            context ={
                'message':'SuccessFully deleted Product'
            }
            return Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context ={
                'message':'Invalid Product_id'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)




