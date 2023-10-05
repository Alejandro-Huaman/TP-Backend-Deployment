from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from apps.resultSection.models import ResultSection
from apps.resultSection.api.serializer import ResultSectionSerializer
from rest_framework.decorators import action

    
class ResultSectionViewSets(viewsets.ModelViewSet):
    model = ResultSection
    serializer_class = ResultSectionSerializer
    queryset = None
    def get_object(self, pk):
            return get_object_or_404(self.model, pk=pk)
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.get_serializer().Meta.model.objects.filter(state=True)
        return self.queryset
    def list(self, request):
        question_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "rows": question_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, pk=None):
        section = self.get_object(pk)
        question_serializer = self.serializer_class(section)
        return Response(question_serializer.data)

    def destroy(self, request, pk=None):
        user_destroy = self.model.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({
                'message': 'pregunta eliminado correctamente'
            })
        return Response({
            'message': 'No existe la pregunta que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)
    @action(detail=True, methods=['get'])
    def getResultSectionbySection(self,request,pk=None):
       
        self.queryset = self.serializer_class().Meta.model.objects.filter(state=True).filter(section_id=pk)
        ResultSection = self.get_queryset()
        ResultSection_serializer = self.serializer_class(ResultSection, many=True)
        data = {
            
            "total": self.get_queryset().count(),
            "rows": ResultSection_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    @action(detail=True, methods=['get'])
    def getResultSectionbyResultTest(self,request,pk=None):
       
        self.queryset = self.serializer_class().Meta.model.objects.filter(state=True).filter(resultTest_id=pk)
        ResultTest= self.get_queryset()
        ResultTest_serializer = self.serializer_class(ResultTest, many=True)
        data = {
            
            "total": self.get_queryset().count(),
            "rows": ResultTest_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    @action(detail=False, methods=['get'])
    def getResultSectionbyTestAndResultTest(self, request, test_id, result_test_id):
        result_sections = ResultSection.objects.filter(
            section__test_id=test_id, resultTest_id=result_test_id, state=True
        )
        
        result_sections_serializer = self.serializer_class(result_sections, many=True)
        
        data = {
            "total": result_sections.count(),
            "rows": result_sections_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    