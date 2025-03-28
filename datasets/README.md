# ABOUT DATASETS FOR CHATDOCTOR ASSISTANT

Các bộ dữ liệu được chọn bao gồm:


- [GitHub - abachaa/MedQuAD: Medical Question Answering Dataset of 47,457 QA pairs created from 12 NIH websites](https://github.com/abachaa/MedQuAD)
- [TsinghuaC3I/MedXpertQA · Datasets at Hugging Face](https://huggingface.co/datasets/TsinghuaC3I/MedXpertQA)

# 1. Introduction

- Giới thiệu ngắn gọn về các bộ dataset

# 2. About datasets

## 2.1. [lavita/medical-eval-sphere](https://huggingface.co/datasets/lavita/medical-eval-sphere)

Đây là một bộ dataset để đánh giá các tiêu chí dành cho các mô hình LLM khi trả lời các câu hỏi liên quan đến y tế. Bộ dữ liệu này chứa các id, câu hỏi các model LLM và đi kèm với các phản hồi của nó. Bộ dữ liệu này khoảng 400 dòng với ngôn ngữ tiếng Anh.

## 2.2. [lavita/ChatDoctor-HealthCareMagic-100k](https://huggingface.co/collections/lavita/medical-qa-datasets-6540b9b1992b1c560eda935c)

Bộ dữ liệu này có 112,165 dòng bằng tiếng Anh. Trong đó, mỗi dòng có 3 cột đó là Instruction, Input là các câu hỏi và Output là các câu trả lời tương ứng.  Để xem thêm các thông tin về dataset này, xem tại đây [here](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)

## 2.3. [lavita/ChatDoctor-iCliniq](https://huggingface.co/datasets/lavita/ChatDoctor-iCliniq)

Bộ dữ liệu này có 7,321 dòng và 4 cột. Trong đó, cột input là những câu hỏi, 3 cột còn lại các các câu trả lời của các mô hình khác nhau.

## 2.4. [medalpaca/medical_meadow_medical_flashcards](https://huggingface.co/datasets/medalpaca/medical_meadow_medical_flashcards)

Bộ dữ liệu này chứa các hướng dẫn, câu hỏi và câu trả lời tương ứng, với 33,955 dòng. Các thẻ ghi nhớ Anki Medical Curriculum được sinh viên y khoa tạo ra và cập nhật và bao gồm toàn bộ chương trình giảng dạy này, giải quyết các môn học như giải phẫu, sinh lý, bệnh lý, dược lý, v.v. Các thẻ ghi nhớ này thường có tóm tắt ngắn gọn và phương pháp ghi nhớ để hỗ trợ việc học và ghi nhớ các khái niệm y khoa quan trọng.

## 2.5. [medalpaca/medical_meadow_wikidoc](https://huggingface.co/datasets/medalpaca/medical_meadow_wikidoc)

Bộ dữ liệu này chứa các cặp câu hỏi-trả lời y khoa được trích xuất từ WikiDoc, một nền tảng cộng tác dành cho các chuyên gia y khoa để chia sẻ và đóng góp vào kiến thức y khoa mới nhất. Sau đó sử dụng GTP-3.5-Turbo để diễn đạt lại tiêu đề đoạn văn thành một câu hỏi và sử dụng đoạn văn đó làm câu trả lời. Bộ dữ liệu này có khoảng 10k dòng, với các hướng dẫn, input chứa các câu hỏi và output là các câu trả lời.

## 2.6. [medalpaca/medical_meadow_medqa](https://huggingface.co/datasets/medalpaca/medical_meadow_medqa)

Dữ liệu chứa cả QA và sách giáo khoa có thể được tải xuống từ thư mục Google Drive này. Một số thông tin chi tiết về dữ liệu được giải thích như sau: Đối với QA, chúng tôi có ba nguồn: Hoa Kỳ, Trung Quốc đại lục và Đài Loan, được đặt trong các thư mục tương ứng. Tất cả các tệp cho QA đều ở định dạng tệp jsonl, trong đó mỗi dòng là một mẫu dữ liệu dưới dạng dict. Các tệp "XX_qbank.jsonl" chứa tất cả các mẫu dữ liệu trong khi chúng tôi cũng cung cấp một bản phân chia ngẫu nhiên chính thức thành các tập huấn luyện, phát triển và kiểm tra. Các tệp đó trong thư mục "metamap" được trích xuất các cụm từ liên quan đến y tế bằng công cụ Metamap. Đối với QA, chúng tôi cũng bao gồm phiên bản "4_options" cho Hoa Kỳ và Trung Quốc đại lục vì chúng tôi đã báo cáo kết quả cho 4 tùy chọn trong bài báo. Đối với sách giáo khoa, chúng tôi có hai ngôn ngữ: tiếng Anh và tiếng Trung giản thể. Đối với tiếng Trung giản thể, chúng tôi cung cấp hai loại phân chia câu: một là phân chia theo câu và loại còn lại là phân chia theo đoạn văn.

## 2.7. [medalpaca/medical_meadow_mediqa](https://huggingface.co/datasets/medalpaca/medical_meadow_mediqa)

Bộ dữ liệu này có 2,208 dòng với instruction, input là các câu hỏi và output là các câu trả lời.

## 2.8. [medalpaca/medical_meadow_cord19](https://huggingface.co/datasets/medalpaca/medical_meadow_cord19)

Để ứng phó với đại dịch COVID-19, Nhà Trắng và liên minh các nhóm nghiên cứu hàng đầu đã chuẩn bị Bộ dữ liệu nghiên cứu mở về COVID-19 (CORD-19). CORD-19 là nguồn tài nguyên gồm hơn 1.000.000 bài báo khoa học, bao gồm hơn 400.000 bài có toàn văn, về COVID-19, SARS-CoV-2 và các loại vi-rút corona liên quan. Bộ dữ liệu có sẵn miễn phí này được cung cấp cho cộng đồng nghiên cứu toàn cầu để áp dụng những tiến bộ gần đây trong xử lý ngôn ngữ tự nhiên và các kỹ thuật AI khác để tạo ra những hiểu biết mới nhằm hỗ trợ cuộc chiến đang diễn ra chống lại căn bệnh truyền nhiễm này. Đây là phiên bản đã xử lý của bộ dữ liệu, trong đó chúng tôi đã xóa một số mục nhập trống và định dạng để tương thích với chương trình đào tạo alpaca. Để biết thêm chi tiết về dữ liệu, vui lòng tham khảo ấn phẩm gốc.

Bộ dữ liệu này có [821,007]() dòng với các cột chính là input, output và instruction.

## 2.9. [medalpaca/medical_meadow_mmmlu](https://huggingface.co/datasets/medalpaca/medical_meadow_mmmlu)

Bộ dữ liệu này chứa các câu hỏi trắc nghiệm và đi kèm với các đáp án, với 3,787 dòng.

## 2.10. [bigbio/med_qa](https://huggingface.co/datasets/bigbio/med_qa)

Tập dữ liệu OpenQA trắc nghiệm dạng tự do đầu tiên để giải quyết các vấn đề y khoa, MedQA, được thu thập từ các kỳ thi hội đồng y khoa chuyên nghiệp. Nó bao gồm ba ngôn ngữ: tiếng Anh, tiếng Trung giản thể và tiếng Trung phồn thể, và chứa 12.723, 34.251 và 14.123 câu hỏi cho ba ngôn ngữ tương ứng. Cùng với dữ liệu câu hỏi, chúng tôi cũng thu thập và phát hành một kho dữ liệu quy mô lớn từ các sách giáo khoa y khoa mà từ đó các mô hình hiểu đọc có thể thu thập được kiến thức cần thiết để trả lời các câu hỏi.

## 2.11. [bigbio/pubmed_qa](https://huggingface.co/datasets/bigbio/pubmed_qa)

**PubMedQA** là bộ dữ liệu Hỏi-Đáp y sinh từ PubMed, giúp trả lời câu hỏi nghiên cứu bằng  **Yes/No/Maybe** . Mỗi mẫu gồm  **câu hỏi** ,  **ngữ cảnh (tóm tắt nghiên cứu không có kết luận)** , **câu trả lời dài (kết luận nghiên cứu)** và  **câu trả lời ngắn** .

Bộ dữ liệu gồm:

* **PQA-L** : 1k mẫu có nhãn thủ công.
* **PQA-A** : 211.3k mẫu tạo tự động.
* **PQA-U** : 61.2k mẫu chưa gán nhãn.

Đây là bộ QA đầu tiên yêu cầu suy luận trên văn bản nghiên cứu y sinh.

## 2.12. [hyesunyun/liveqa_medical_trec2017](https://huggingface.co/datasets/hyesunyun/liveqa_medical_trec2017)

Thẻ dữ liệu cho LiveQA Medical từ TREC 2017 Nhiệm vụ y tế LiveQA'17 tập trung vào việc trả lời câu hỏi về sức khỏe của người tiêu dùng. Thư viện Y khoa Quốc gia Hoa Kỳ (NLM) đã nhận được các câu hỏi về sức khỏe của người tiêu dùng. Bộ dữ liệu bao gồm các cặp câu hỏi-trả lời y tế được xây dựng để đào tạo và kiểm tra, với các chú thích bổ sung có thể được sử dụng để phát triển phân tích câu hỏi và hệ thống trả lời câu hỏi. Bộ dữ liệu này có khoảng 104 dòng.

## 2.13. [stellalisy/MediQ_AskDocs](https://huggingface.co/datasets/stellalisy/MediQ_AskDocs)

Bộ dữ liệu này là tập dữ liệu SFT của MediQ_AskDocs với khoảng 46.8k dòng là những câu hỏi và trả lời liên quan đến sức khỏe y khoa.

## 2.14. [stellalisy/mediQ](https://huggingface.co/datasets/stellalisy/mediQ/viewer/default/validation?row=0)

Bộ dữ liệu này có 2,545 dòng bao gồm các miêu tả sức khỏe trường hợp cụ thể và các đề xuất thuốc.

## 2.15. [MeQuaAD](https://github.com/abachaa/MedQuAD)

MedQuAD bao gồm 47.457 cặp câu hỏi-trả lời y khoa được tạo từ 12 trang web của NIH (ví dụ: cancer.gov, niddk.nih.gov, GARD, MedlinePlus Health Topics). Bộ sưu tập bao gồm 37 loại câu hỏi (ví dụ: Điều trị, Chẩn đoán, Tác dụng phụ) liên quan đến bệnh tật, thuốc và các thực thể y khoa khác như xét nghiệm.

# 3. Final dataset
