# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Category, VideoFile, Video

# # Create your tests here.
# class CategoryModelTest(TestCase):

#     def setUp(self):
#         self.category = Category.objects.create(name='Test Category')

#     def test_category_creation(self):
#         category = Category.objects.get(name='Test Category')
#         self.assertEqual(category.name, 'Test Category')
#         self.assertEqual(str(category), 'Test Category')

# class VideoFileModelTest(TestCase):

#     def setUp(self):
#         self.video_file = VideoFile.objects.create(
#             videofile='deploy/videos/2023/07/25/test_video.mp4',
#             slug='test-video',
#             title='Test Video',
#             discription='This is a test video.',
#             season=1,
#             status=True,
#             counted_views=100
#         )

#     def test_video_file_creation(self):
#         video_file = VideoFile.objects.get(slug='test-video')
#         self.assertEqual(video_file.title, 'Test Video')
#         self.assertEqual(video_file.discription, 'This is a test video.')
#         self.assertEqual(video_file.season, 1)
#         self.assertEqual(video_file.status, True)
#         self.assertEqual(video_file.counted_views, 100)

# class VideoModelTest(TestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='12345')
#         self.category = Category.objects.create(name='Test Category')
#         self.video_file = VideoFile.objects.create(
#             videofile='deploy/videos/2023/07/25/test_video.mp4',
#             slug='test-video',
#             title='Test Video',
#             discription='This is a test video.',
#             season=1,
#             status=True,
#             counted_views=100
#         )
#         self.video = Video.objects.create(
#             slug='test-video',
#             title='Test Video',
#             discription='This is a test video description.',
#             author=self.user,
#             status=True,
#             counted_views=200
#         )
#         self.video.video.add(self.video_file)
#         self.video.category.add(self.category)

#     def test_video_creation(self):
#         video = Video.objects.get(slug='test-video')
#         self.assertEqual(video.title, 'Test Video')
#         self.assertEqual(video.discription, 'This is a test video description.')
#         self.assertEqual(video.author.username, 'testuser')
#         self.assertEqual(video.status, True)
#         self.assertEqual(video.counted_views, 200)
#         self.assertEqual(video.category.first().name, 'Test Category')
#         self.assertEqual(video.video.first().title, 'Test Video')

#     def test_video_str_method(self):
#         video = Video.objects.get(slug='test-video')
#         self.assertEqual(str(video), f'{video.title}: {video.id}')

#     def test_get_absolute_url(self):
#         video = Video.objects.get(slug='test-video')
#         self.assertEqual(video.get_absolute_url(), f'/deploy/detail/{video.slug}/')
