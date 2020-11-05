from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from webprofiles.models import EmployeeProfiles
from webprofiles.serializers import EmployeeSerializer


# its a general class to create and get the data
class EmployeeView(APIView):

    # this function returns all the data
    def get(self, request):
        emp_obj = EmployeeProfiles.objects.all()
        emp_serialize_obj = EmployeeSerializer(emp_obj, many=True)
        return Response(emp_serialize_obj.data, status=status.HTTP_200_OK)

    # this method creates the new object
    def post(self, request):
        serialize_obj = EmployeeSerializer(data=request.data)
        if serialize_obj.is_valid():
            serialize_obj.save()
            return Response(serialize_obj.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# below part is for upgradation purpose and to retrieve specific details

class EmployeeUpdate(APIView):

    def get_object(self, pk):
        # it block checks if that 'pk' does have any value that can be used futher
        try:
            return EmployeeProfiles.objects.get(pk=pk)
        except EmployeeProfiles.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request, pk):
        # this function gets a detail of a single object
        emp_obj = self.get_object(pk)
        serialize_obj = EmployeeSerializer(emp_obj)
        return Response(serialize_obj.data)

    def put(self, request, pk):
        # ''' This function updates a particular object details'''
        emp_obj = self.get_object(pk)
        emp_serialize = EmployeeSerializer(emp_obj, default=request.data)
        if emp_serialize.is_valid():
            emp_serialize.save()
            return Response(emp_serialize.data, status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # ''' This function shits a particular object'''
        emp_obj = self.get_object(pk)
        emp_obj.delete()
        return Response(status=status.HTTP_200_OK)
