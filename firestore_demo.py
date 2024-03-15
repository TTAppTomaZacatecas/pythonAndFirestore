import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#from google.cloud.firestore_v1.base_query import FieldFilter,Or
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

#data = {
#    "field1": "los miios",
#    "field2": "los mios 2",
#    "field3": "fk3io434"
#}

#doc_ref = db.collection("dbtest1").document()
#doc_ref.set(data)

#print("Document ID", doc_ref.id)

def get_all_docs(collectionName):
    docs = (
        db.collection(collectionName)
        .stream()
    )

    documents_list = []
    for doc in docs:
        doc_data = doc.to_dict()
        doc_data['id'] = doc.id
        doc_data['docData'] = doc._data
        documents_list.append(doc_data)

    for doc_data in documents_list:
        print(f"Document ID: {doc_data['id']}")
        print(f"Document Data: {doc_data['docData']}")
        print()


def get_document(collection_name, document_id):
    doc_ref = db.collection(collection_name).document(document_id)
    print(doc_ref)
    doc = doc_ref.get()
    print(doc)
    if doc.exists:
        return doc.to_dict()
    else:
        print(f"Document '{document_id}' not found in collection '{collection_name}'")
        return None



#get_all_docs("dbtest1")
print(get_document("dbtest1", "HRoCAEf3S7jpCfSUXTwW"))
print(get_document("dbtest1", "bXjt91rJtiLHWVbHzxIx"))
print(get_document("dbtest1", "doc1"))