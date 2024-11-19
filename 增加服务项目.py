import json

import requests

from config import headers


def get_price_list(page=1,pageSize=10):
  url ='http://192.168.26.1/kapi/hbos-hsc/admin/price/page'
  data={
  "current":1,
  "size":10,
  "keyword":"测试",
  "isSortUpdateTime":None
}
  resp = requests.post(url, headers=headers, data=json.dumps(data))
  print(resp.json())
#新建物价
def create_new_price(code,price_name,countryPriceCode,unit="",price=100,childrenPrice=0,medicalInsurancePrice=0,hospitalType=3,nationalMedicareCode="",provincialMedicareCode=""):
  """
  :param code: 系统编码*
  :param price_name:物价名称*
  :param countryPriceCode:医保编码*
  :param nationalMedicareCode:国家医保编码
  :param provincialMedicareCode:省医保编码
  :param price:价格*
  :param childrenPrice:儿童价格
  :param medicalInsurancePrice:医保价格
  :param unit:单位*
  :param hospitalType:医院类型
  :return:
  """
  url ='http://192.168.26.1/kapi/hbos-hsc/admin/price/create'
  data={
  "id":0,
  "key":"0",
  "code":code,
  "name":price_name,
  "countryPriceCode":countryPriceCode,
  "nationalMedicareCode":nationalMedicareCode,
  "provincialMedicareCode":provincialMedicareCode,
  "hospitalType":hospitalType,
  "hospitalTypeDesc":"",
  "price":price,
  "childrenPrice":childrenPrice,
  "medicalInsurancePrice":medicalInsurancePrice,
  "unit":unit,
  "effectiveTime":"2024-11-19 23:20:30",
  "expireTime":"2124-11-19 23:20:30",
  "priceSource":0,#0:国家定价，1:医院定价
  "priceSourceDesc":"",
  "status":2,#2:启用，1:停用
  "statusDesc":"",
  "description":""
}

  response = requests.post(url, headers=headers, data=json.dumps(data))

  if response.status_code == 200:
    print("创建物价成功")

  else:
    print("创建物价失败")
  print(response.json())


# 计费科目
def get_subjectList():
  url='http://192.168.26.1/kapi/hbos-hsc/admin/common/getSubjectList'
  data=""
  resp_data = requests.post(url, headers=headers, data=data).json()['data']
  print(resp_data)

#计费模版
def get_billingTemplate():
  url='http://192.168.26.1/kapi/hbos-hsc/admin/chargeItem/billingTemplate/list'
  data=""
  resp_data = requests.post(url, headers=headers, data=data).json()['data']
  return resp_data

def convertChargeItemByPrice(priceId,subjectCode='0',billingTemplateCode="basis"):
  url='http://192.168.26.1/kapi/hbos-hsc/admin/price/convertChargeItemByPrice'

  data={
  "priceId":priceId,
  "subjectCode":subjectCode,
  "billingTemplateCode":billingTemplateCode
}

  response = requests.post(url, headers=headers, data=json.dumps(data))
  if response.status==200:
    print("转换计费项成功")
  print(response.json())



def set_service_project(name,unitCode,chargeItemCode):

  url = "http://192.168.26.1/kapi/hbos-hsc/admin/serviceItem/operation/save"
  data={
  "materialAdditions":[ ],
  "medicineAdditions":[ ],
  "serviceAdditions":[ ],
  "examinationInfo":{
    "informedConsentTemplateCodesForOutPatient":[ ],
    "informedConsentTemplateCodesForInPatient":[ ],
    "informedConsentTemplateIdsForOutPatient":[ ],
    "informedConsentTemplateIdsForInPatient":[ ],
    "attentionInfo":{
      "foodProhibitedHours":0,
      "attentionCodes":[ ],
      "attentionExtra":""
    },
    "isAdmissionDoctorOrder":0,
    "needAnesthesiaConsultant":0,
    "defaultFrequencyCode":"",
    "billingBodyPartNum":1,
    "frequencyTypeCodes":[ ],
    "subCategoryCode":"",
    "isUrgent":0,
    "patientLimits":[ ],
    "genderLimit":0,
    "isRelation":0,
    "relationServices":[ ],
    "isMetalImplantation":0,
    "evaluationList":[ ],
    "isBedside":0,
    "isReferral":0,
    "isAppointment":0,
    "specialDiseases":[ ],
    "supportNursingOrder":0,
    "mutualRecognitionCodeList":[ ],
    "indication":"",
    "contraindication":"",
    "isAutoEject":0
  },
  "labTestInfo":{
    "informedConsentTemplateCodesForOutPatient":[ ],
    "informedConsentTemplateCodesForInPatient":[ ],
    "informedConsentTemplateIdsForOutPatient":[ ],
    "informedConsentTemplateIdsForInPatient":[ ],
    "attentionInfo":{
      "foodProhibitedHours":0,
      "attentionCodes":[ ],
      "attentionExtra":""
    },
    "isAdmissionDoctorOrder":0,
    "needDeliveryOut":0,
    "defaultFrequencyCode":"",
    "frequencyTypeCodes":[ ],
    "isUrgent":0,
    "sampleTypeCode":"",
    "sampleTypeList":[ ],
    "containerCode":"",
    "patientLimits":[ ],
    "genderLimit":0,
    "subCategoryCode":"",
    "specialDiseases":[ ],
    "supportNursingOrder":0,
    "mutualRecognitionCodeList":[ ],
    "isAutoEject":0
  },
  "therapyInfo":{
    "patientLimits":[ ],
    "genderLimit":0,
    "needEvaluate":0,
    "isHighRisk":0,
    "isContinuous":0,
    "isUrgent":0,
    "frequencyTypeCodes":[ ],
    "defaultFrequencyCode":"",
    "informedConsentTemplateCodesForOutPatient":[ ],
    "informedConsentTemplateCodesForInPatient":[ ],
    "informedConsentTemplateIdsForOutPatient":[ ],
    "informedConsentTemplateIdsForInPatient":[ ],
    "appointmentResourceCountCost":1,
    "needAppoint":1,
    "specialDiseases":[ ],
    "supportNursingOrder":0
  },
  "boneMarrowInfo":{
    "needInfectiousDiseaseScreening":0,
    "genderLimit":0,
    "sampleType":"",
    "frequencyTypeCodes":[ ],
    "subCategoryCode":"",
    "defaultFrequencyCode":"",
    "attentionInfo":{
      "foodProhibitedHours":0,
      "attentionCodes":[ ],
      "attentionExtra":""
    },
    "specialDiseases":[ ],
    "supportNursingOrder":0
  },
  "pathologyInfo":{
    "needInfectiousDiseaseScreening":0,
    "genderLimit":0,
    "sampleType":"",
    "frequencyTypeCodes":[ ],
    "subCategoryCode":"",
    "defaultFrequencyCode":"",
    "attentionInfo":{
      "foodProhibitedHours":0,
      "attentionCodes":[ ],
      "attentionExtra":""
    },
    "informedConsentTemplateIdsForOutPatient":[ ],
    "informedConsentTemplateIdsForInPatient":[ ],
    "applyTemplateCode":"",
    "specialDiseases":[ ],
    "supportNursingOrder":0
  },
  "surgeryInfo":{
    "surgeryLevel":"1",
    "icdCode":"",
    "icdType":"",
    "isAmbulatorySurgery":0,
    "incisionType":"",
    "isImportantAndDifficultSurgery":0,
    "defaultFrequencyCode":"PC-000000003",
    "informedConsentTemplateCodesForOutPatient":[ ],
    "informedConsentTemplateCodesForInPatient":[ ],
    "informedConsentTemplateIdsForOutPatient":[ ],
    "informedConsentTemplateIdsForInPatient":[ ],
    "attentionInfo":{
      "foodProhibitedHours":0,
      "attentionCodes":[ ],
      "attentionExtra":""
    },
    "departmentsOrderAllowed":{
      "allAllowed":0,
      "deptIdsAllowed":[ ]
    }
  },
  "managementInfo":{
    "exclusionType":0,
    "frequencyTypeCodes":[ ],
    "defaultFrequencyCode":"",
    "specialDiseases":[ ],
    "supportNursingOrder":0
  },
  "skinTestInfo":{ },
  "bloodMakingInfo":{
    "isDefaultBloodMakingService":0
  },
  "adviceInfo":{
    "exclusionType":0,
    "frequencyTypeCodes":[ ],
    "defaultFrequencyCode":"",
    "specialDiseases":[ ],
    "supportNursingOrder":0
  },
  "normalTreatmentInfo":{
    "exclusionType":0,
    "frequencyTypeCodes":[
      "FH0110.01",
      "FH0110.02",
      "FH0110.03",
      "FH0110.04",
      "FH0110.05",
      "FH0110.06"
    ],
    "defaultFrequencyCode":"PC010000001ST",
    "isAutoExecution":0,
    "informedConsentTemplateIdsForOutPatient":[ ],
    "informedConsentTemplateIdsForInPatient":[ ],
    "isBillLimit":0,
    "billLimitCodes":[ ],
    "specialDiseases":[ ],
    "supportNursingOrder":0
  },
  "nursingNormalInfo":{
    "exclusionType":0,
    "frequencyTypeCodes":[ ],
    "defaultFrequencyCode":"",
    "isAutoExecution":0,
    "informedConsentTemplateIdsForOutPatient":[ ],
    "informedConsentTemplateIdsForInPatient":[ ],
    "specialDiseases":[ ],
    "supportNursingOrder":0
  },
  "physicalExaminationInfo":{
    "frequencyTypeCodes":[ ],
    "defaultFrequencyCode":""
  },
  "consultationInfo":{
    "frequencyTypeCodes":[ ],
    "defaultFrequencyCode":"",
    "consultationTemplateIdForOutPatient":"",
    "consultationTemplateIdForInPatient":"",
    "specialDiseases":[ ],
    "supportNursingOrder":0,
    "practiceTypes":[ ],
    "professionalTitles":[ ]
  },
  "bloodProductInfo":{
    "frequencyTypeCodes":[ ],
    "defaultFrequencyCode":"",
    "bloodProductType":""
  },
  "appointmentResourceInfo":{
    "doctorProfessionalCode":"",
    "freeDiagnose":0
  },
  "medicationServiceInfo":{
    "informedConsentTemplateIdsForOutPatient":[ ],
    "informedConsentTemplateIdsForInPatient":[ ]
  },
  "chargeItems":[
    {
      "chargeItemCode":chargeItemCode,
      "billingMethod":0,
      "quantity":1,
      "needChargeSceneCodes":[ ],
      "isEdit":True
    }
  ],
  "healthcareSceneDoctorOrderLimitations":[
    {
      "campusId":"30044002",
      "campusName":"桂平市人民医院",
      "forOutpatient":1,
      "forInpatient":1,
      "forEmergency":1,
      "forEmergencyObservation":1,
      "forEmergencyRescue":1,
      "forOutpatientPhysicalExamination":1,
      "forInpatientPhysicalExamination":1
    },
    {
      "campusId":"30044003",
      "campusName":"桂平市人民医院(江北院区)",
      "forOutpatient":1,
      "forInpatient":1,
      "forEmergency":1,
      "forEmergencyObservation":1,
      "forEmergencyRescue":1,
      "forOutpatientPhysicalExamination":1,
      "forInpatientPhysicalExamination":1
    },
    {
      "campusId":"30051147",
      "campusName":"桂平市人民医院第二门诊部",
      "forOutpatient":1,
      "forInpatient":1,
      "forEmergency":1,
      "forEmergencyObservation":1,
      "forEmergencyRescue":1,
      "forOutpatientPhysicalExamination":1,
      "forInpatientPhysicalExamination":1
    }
  ],
  "subCategoryCode":"",
  "extraInfo":{ },
  "id":None,
  "managementCategoryCode":"FH0101.04.01.03",#管理类目
  "managementCategoryCodes":[ ],
  "managementCategoryName":"其他",
  "code":"NT-110208001",#编码，自定义
  "name":name,
  "pinyinCode":"CS1",
  "searchCode":"IY1",
  "introduction":"",
  "isEnterDoctorOrder":1,
  "unit":"",
  "unitCode":unitCode,
  "status":1,#0:停用，1:启用
  "isCharge":1,
  "externalCode":"外部编码",

  "extraMap":{ },
  "isCountReferencePrice":True#自动执行
}

























def main():

    #创建物价
    price_item = create_new_price(code='1',price_name='测试',countryPriceCode='001',unit='次',price=10)
    #转换成收费项目
    convertChargeItemByPrice(price_item['priceId'],subjectCode='0',billingTemplateCode='basis')






if __name__ == '__main__':
  main()
  # print(headers)
  # get_price_list()

