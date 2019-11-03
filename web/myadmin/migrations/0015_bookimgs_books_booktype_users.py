# Generated by Django 2.2.3 on 2019-10-21 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myadmin', '0014_auto_20191021_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booktype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catename', models.CharField(max_length=20)),
                ('pid', models.IntegerField()),
                ('path', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('password', models.CharField(max_length=80)),
                ('face', models.CharField(default='/static/myadmin/assets/img/user06.png', max_length=100)),
                ('nickname', models.CharField(max_length=20, null=True)),
                ('homeaddress', models.CharField(max_length=100, null=True)),
                ('sex', models.CharField(max_length=6, null=True)),
                ('usertype', models.CharField(max_length=1, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('isdel', models.CharField(default='004001', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=70)),
                ('recommend', models.CharField(max_length=255, null=True)),
                ('author', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=150)),
                ('pdate', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('num', models.IntegerField()),
                ('isbn', models.CharField(max_length=13)),
                ('bookdetail', models.TextField(null=True)),
                ('cate', models.CharField(default='0', max_length=1)),
                ('isdel', models.CharField(default='004001', max_length=6)),
                ('typeid', models.ManyToManyField(to='myadmin.Booktype')),
            ],
        ),
        migrations.CreateModel(
            name='Bookimgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.ImageField(upload_to='static/myadmin/book_img/')),
                ('bookid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.Books')),
            ],
        ),
    ]