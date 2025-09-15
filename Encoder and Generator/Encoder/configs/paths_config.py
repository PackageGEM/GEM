dataset_paths = {
	'celeba_train': '',
	'celeba_test': '/home/tyuah/projects/pixel2style2pixel/data/test',
	'celeba_train_sketch': '',
	'celeba_test_sketch': '',
	'celeba_train_segmentation': '',
	'celeba_test_segmentation': '',
	'ffhq': '/home/tyuah/projects/pixel2style2pixel/data/train',
}

model_paths = {
	'stylegan_ffhq': '/home/tyuah/projects/pixel2style2pixel/logs/460000.pt',
	'ir_se50': '/home/tyuah/projects/pixel2style2pixel/logs/model_ir_se50.pth',
	'circular_face': 'pretrained_models/CurricularFace_Backbone.pth',
	'mtcnn_pnet': 'pretrained_models/mtcnn/pnet.npy',
	'mtcnn_rnet': 'pretrained_models/mtcnn/rnet.npy',
	'mtcnn_onet': 'pretrained_models/mtcnn/onet.npy',
	'shape_predictor': 'shape_predictor_68_face_landmarks.dat',
	'moco': 'pretrained_models/moco_v2_800ep_pretrain.pth.tar'
}
