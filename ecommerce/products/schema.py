import graphene
from graphene_django import DjangoObjectType
from .models import Category, Book, Grocery


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'title')


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'isbn', 'pages', 'price',
                  'quantity', 'description', 'status', 'date_created')


class GroceryType(DjangoObjectType):
    class Meta:
        model = Grocery
        fields = ('id', 'product_tag', 'name', 'category',
                  'price', 'quantity', 'imageurl', 'date_created')


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    books = graphene.List(BookType)
    groceries = graphene.List(GroceryType)

    def resolve_categories(self, info, **kwargs):
        # Quering a list of all categories
        return Category.objects.all()

    def resolve_books(self, info, **kwargs):
        # Quering a list of all books
        return Book.objects.all()

    def resolve_groceries(self, info, **kwargs):
        # Quering a list of all groceries
        return Grocery.objects.all()


class UpdateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to update a category
        title = graphene.String(required=True)
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title, id):
        category = Category.objects.get(pk=id)
        category.title = title
        category.save()

        return UpdateCategory(category=category)


class CreateCategory(graphene.Mutation):
    class Arguments:
        # Mutation to create a category
        title = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, title):
        category = Category()
        category.title = title
        category.save()

        return CreateCategory(category=category)


class BookInput (graphene.InputObjectType):
    title = graphene.String()
    author = graphene.String()
    pages = graphene.Int()
    price = graphene.Float()
    quantity = graphene.Int()
    description = graphene.String()
    status = graphene.String()


class CreateBook (graphene.Mutation):
    class Arguments:
        # Mutation to create a book
        input = BookInput(required=True)

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, input):
        book = Book()
        book.title = input.title
        book.author = input.author
        book.pages = input.pages
        book.price = input.price
        book.quantity = input.quantity
        book.description = input.description
        book.status = input.status
        book.save()
        return CreateBook(book=book)


class UpdateBook (graphene.Mutation):
    class Arguments:
        # Mutation to update a book
        input = BookInput(required=True)
        id = graphene.ID()

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, input, id):
        book = Book.objects.get(pk=id)
        book.name = input.name
        book.description = input.description
        book.price = input.price
        book.quantity = input.quantity
        book.save()
        return UpdateBook(book=book)


class GroceryInput (graphene.InputObjectType):
    product_tag = graphene.String()
    name = graphene.String()
    category = graphene.String()
    price = graphene.Float()
    quantity = graphene.Int()
    imageurl = graphene.String()


class CreateGrocery (graphene.Mutation):
    class Arguments:
        # Mutation to create a grocery
        input = GroceryInput(required=True)
        id = graphene.ID()

    grocery = graphene.Field(GroceryType)

    @classmethod
    def mutate(cls, root, info, input, id):
        grocery = Grocery()
        grocery.product_tag = input.product_tag
        grocery.name = input.name
        grocery.category = input.category
        grocery.price = input.price
        grocery.quantity = input.quantity
        grocery.imageurl = input.imageurl
        grocery.save()
        return CreateGrocery(grocery=grocery)


class UpdateGrocery (graphene.Mutation):
    class Arguments:
        # Mutation to update a grocery
        input = GroceryInput(required=True)
        id = graphene.ID()

    grocery = graphene.Field(GroceryType)

    @classmethod
    def mutate(cls, root, info, input, id):
        grocery = Grocery.objects.get(pk=id)
        grocery.product_tag = input.product_tag
        grocery.name = input.name
        grocery.category = input.category
        grocery.price = input.price
        grocery.quantity = input.quantity
        grocery.imageurl = input.imageurl
        grocery.save()
        return UpdateGrocery(grocery=grocery)


class Mutation (graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


# for create a new category past this code in left side of Graphql playground
# mutation {
#  create_category:createCategory(title :"Plastic") {
#   category {
#    id,
#    title,
#   }
#  }
# }

# for Create book past this code in left side of Graphql playground
# mutation {
#   create_book: createBook(input: {title:"Imagine this",author: "Shola", pages: 12, price: 1200, quantity: 4, description:"a brief description", status: "True"}){
#     book {
#       id,
#       title,
#       author,
#       pages,
#       price,
#       quantity,
#       description,
#       status
#     }
#   }
# }
